from django.db import models


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
    Groupq
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
    p_large = models.FloatField()
    num_extra = models.IntegerField()
    extras = models.ManyToManyField(ExtraIngridient, through="MenuCombination", related_name="dishes")
    # extras = models.ManyToManyField(ExtraIngridient)

    def __str__(self):
        return "{} {}".format(self.name, self.group)


class MenuCombination(models.Model):
    extra = models.ForeignKey(ExtraIngridient, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    price = models.FloatField()
