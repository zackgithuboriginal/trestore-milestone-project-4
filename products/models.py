from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category  = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=254)
    sku =  models.CharField(max_length=254, null=True, blank=True)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name