from django import forms

from .models import Profile


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'bio', 'avatar', 'cover_image')
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"}),
            'bio': forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5
            }),
            # 'uid_division': forms.Select(attrs={"class": "form-control"}),

        }
