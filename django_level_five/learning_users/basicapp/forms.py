from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('porfolio_site', 'profile_pic')

class PostForm(forms.Form):
    post = forms.CharField(max_length=256)
