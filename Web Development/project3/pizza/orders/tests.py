from django.test import TestCase

from orders.models import Group, ExtraIngridient, MenuItem, MenuCombination, Order, MenuItemChoice
from django.contrib.auth.models import User

class OrderTestCase(TestCase):
    def setUp(self):
        pizza_group = Group.objects.create(type="pizza")
        sub_group = Group.objects.create(type="sub")

        tomatoe = ExtraIngridient.objects.create(name="tomatoe")
        olives = ExtraIngridient.objects.create(name="olives")
        ham = ExtraIngridient.objects.create(name="ham")
        cheese = ExtraIngridient.objects.create(name="cheese")

        pizza = MenuItem.objects.create(name="pizza",
                                        group=pizza_group,
                                        p_small=5,
                                        p_large=7,
                                        num_extra=2)
        MenuCombination.objects.create(extra=tomatoe,
                                       item=pizza,
                                       price=0)
        MenuCombination.objects.create(extra=olives,
                                       item=pizza,
                                       price=0)
        MenuCombination.objects.create(extra=ham,
                                       item=pizza,
                                       price=0)
        MenuCombination.objects.create(extra=cheese,
                                       item=pizza,
                                       price=0)


        sub = MenuItem.objects.create(name="sub",
                                        group=sub_group,
                                        p_small=5,
                                        num_extra=1)
        MenuCombination.objects.create(extra=tomatoe,
                                       item=sub,
                                       price=0.5)
        MenuCombination.objects.create(extra=olives,
                                       item=sub,
                                       price=0.5)
        MenuCombination.objects.create(extra=ham,
                                       item=sub,
                                       price=2)
        MenuCombination.objects.create(extra=cheese,
                                       item=sub,
                                       price=3)

        user = User.objects.create_user(
            username="Bartek",
            password="pass",
            email="mail@example.pl",
            first_name="Bartek",
            last_name="Smith"
        )

        order = Order.objects.create(user=user,
                                     confirmation=False,
                                     address="Gutanów",
                                     phone="726852322")
        MenuItemChoice.objects.create(item=sub,
                                      order=order,
                                      size="small").extras.set([tomatoe,])
        MenuItemChoice.objects.create(item=sub,
                                      order=order,
                                      size="small").extras.set([ham,])
        MenuItemChoice.objects.create(item=pizza,
                                      order=order,
                                      size="small").extras.set([olives, tomatoe])
        MenuItemChoice.objects.create(item=pizza,
                                      order=order,
                                      size="large").extras.set([ham, tomatoe])




    def test_name(self):
        """Test ability to print correct strings"""
        self.assertEqual(Group.objects.get(type="pizza").__str__(), "pizza")
        self.assertEqual(Group.objects.get(type="sub").__str__(), "sub")

    def test_price(self):
        """Test ability to get a item price"""
        order = Order.objects.get(pk=1)
        self.assertEqual(order.items.through.objects.get(pk=1).get_price(), 5.5)
        self.assertEqual(order.items.through.objects.get(pk=2).get_price(), 7)
        self.assertEqual(order.items.through.objects.get(pk=3).get_price(), 5)
        self.assertEqual(order.items.through.objects.get(pk=4).get_price(), 7)

    def test_total(self):
        """Test ability to get total price of an order"""
        order = Order.objects.get(pk=1)
        self.assertEqual(order.total(), 24.5)
