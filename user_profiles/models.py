from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserProfile(models.Model):
    """
    Model for userprofile object

    Has one to one relation with user object to attach userprofile
    to the user's login and authentication object and details

    Outlines fields relevant to object with necessary restrictions and
    date types
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=50,
                                         null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_postcode = models.CharField(max_length=20,
                                        null=True, blank=True)
    default_county = models.CharField(max_length=80,
                                      null=True, blank=True)
    default_country = CountryField(blank_label="Country",
                                   null=True, blank=True)
    tree_planting_contribution = models.DecimalField(max_digits=10,
                                                     decimal_places=2,
                                                     default=0.00)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Recevier to handle creating or updating a profile
    """
    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()
