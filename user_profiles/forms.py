from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for creating a user model to store delivery details and track orders.

    Creates input fields for all fields of the user profile
    model except for the foreign key user object and
    the tree planting contribution which is tracked passively through the
    checkout view

    Adds necessary attributes and placeholders to each field
    """

    class Meta:
        model = UserProfile
        exclude = ('user', 'tree_planting_contribution')

    def __init__(self, *args, **kwargs):
        """
        Initialises form adds placeholders and necessary attributes
        to input elements
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
