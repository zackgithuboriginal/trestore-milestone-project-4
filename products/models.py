from django.db import models


class Category(models.Model):
    """
    Model for category object

    Specifies verbose plural name for admin

    Outlines fields relevant to object
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model for product object

    Outlines fields relevant to object with
    category as a foreign key field relating to the category
    model
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name
