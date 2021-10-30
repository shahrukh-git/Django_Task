from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Product


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'description']
#         labels = {'title':'Title', 'description':'Description'}
#         widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
#         'description':forms.Textarea(attrs={'class':'form-control'}),}