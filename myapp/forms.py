from django.db.models import fields
from .models import Post, User



# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'description']
#         labels = {'title':'Title', 'description':'Description'}
#         widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
#         'description':forms.Textarea(attrs={'class':'form-control'}),}

from django import forms
from django.forms.widgets import PasswordInput
class SignUpForm(forms.ModelForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=PasswordInput)
        
    class Meta:
        model = User
        fields = '__all__'