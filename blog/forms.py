from django import forms
from products.widgets import CustomClearableFileInput
from .models import ProgressPost, Comment


class AddPostForm(forms.ModelForm):

    class Meta:
        model = ProgressPost
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'post_title': 'Post Title',
            'post_content': 'Post Content',
            'image': 'Image',
            'author': 'Author',
        }

        self.fields['post_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment_content'].widget.attrs['autofocus'] = True
        self.fields[field].widget.attrs['placeholder'] = 'Comment'
