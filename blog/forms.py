from django import forms
from products.widgets import CustomClearableFileInput
from .models import ProgressPost


class AddPostForm(forms.ModelForm):

    class Meta:
        model = ProgressPost
        fields = ('post_title', 'post_content',
                  'image',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'post_title': 'Post Title',
            'post_content': 'Post Content',
        }

        self.fields['post_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'image':
                placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False