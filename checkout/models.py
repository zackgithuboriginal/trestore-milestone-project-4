import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from user_profiles.models import UserProfile


# Create your models here.
class Order(models.Model):
    """ Order model used for tracking details of a customer's order """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    def _generate_order_number(self):
        """
        Method to generate a unique order number for each order
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Method to update the total order cost each time an item is added
        """
        self.order_total = self.lineitems.aggregate(Sum(
                                                    'lineitem_total'))[
                                                    'lineitem_total__sum'] or 0
        self.delivery_cost = ((self.order_total
                              * settings.DELIVERY_PERCENTAGE)
                              / 100)
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Method to check if order has an order number assinged, if not it
        assigns one
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Sub model used to calculate subtotals and track quantities of each product
    """
    order = models.ForeignKey(Order,
                              null=False,
                              blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product,
                                null=False,
                                blank=False,
                                on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False,
                                   blank=False,
                                   default=0)
    lineitem_total = models.DecimalField(max_digits=10,
                                         decimal_places=2,
                                         null=False,
                                         blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Method sets the lineitem total for each item
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU: {self.product.sku} Order: {self.order.order_number}'
