from .models import Post, Comment
from django import forms


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'image')
