from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            if field_name == 'price':
                field.widget.attrs['min'] = '0'
            if field_name == 'product_description':
                field.widget.attrs['rows'] = '4'
            field.widget.attrs['class'] = 'stripe-style-input'
