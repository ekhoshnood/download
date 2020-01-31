from django import forms
from .models import Post

class Create_Post_form(forms.Form):

    class Meta:
        model = Post
        fields = ['text', 'price', 'image']
