from django import forms
from products.widgets import CustomClearableFileInput
from .models import ProgressPost


class AddPostForm(forms.ModelForm):
    """
    Form for adding a progress post
    """
    class Meta:
        model = ProgressPost
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'post_title': 'Post Title',
            'post_content': 'Post Content',
            'author': 'Author',
        }

        self.fields['post_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'image':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
