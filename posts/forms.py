from .models import Post, Comment
from django import forms


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", 'rows': 2}))

    class Meta:
        model = Post
        fields = ('header', 'content', 'image')
        widgets = {
            'header': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5
            }),
        }


class CommentModelForm(forms.ModelForm):
    body = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'placeholder': 'Add a comment...', "class": "form-control "
                                                                                                     "border-0"}))

    class Meta:
        model = Comment
        fields = ('body',)
