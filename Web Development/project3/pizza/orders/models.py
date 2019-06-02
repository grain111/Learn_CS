from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    """
    type of food (Pizza, Sub, Salad, ...)
    """

    type = models.CharField(max_length=64)

    def __str__(self):
        return "{}".format(self.type)


class ExtraIngridient(models.Model):
    """
    Name
    """

    name = models.CharField(max_length=64)

    def __str__(self):
        return "{}".format(self.name)


class MenuItem(models.Model):
    """
    Group
    Name
    AvailbleExtra (Many to Many) with price
    Price for small
    Price for large
    Number of extra ingridients to choose
    """

    name = models.CharField(max_length=64)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="menu_items"
    )
    p_small = models.FloatField()
    p_large = models.FloatField(blank=True, null=True)
    num_extra = models.IntegerField()
    extras = models.ManyToManyField(
        ExtraIngridient, through="MenuCombination", related_name="dishes"
    )

    def __str__(self):
        return "{} {}".format(self.group, self.name)


class MenuCombination(models.Model):
    extra = models.ForeignKey(ExtraIngridient, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    price = models.FloatField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    confirmation = models.BooleanField()
    items = models.ManyToManyField(
        MenuItem, through="MenuItemChoice", related_name="choices"
    )
    timestamp = models.DateField(auto_now_add=True)

    def total(self):
        total = 0
        for item in self.items.through.objects.filter(order=self):
            total += item.get_price()
        return total

    def __str__(self):
        return "An order by {} made at {}".format(self.user, self.timestamp)


class MenuItemChoice(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    extras = models.ManyToManyField(ExtraIngridient)
    size = models.CharField(max_length=5)

    def get_price(self):
        value = self.item.p_small if self.size == "small" else self.item.p_large
        for extra in self.extras.all():
            value += MenuCombination.objects.get(extra=extra, item=self.item).price
        return value
