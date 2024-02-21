from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import MyUser

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = "__all__"

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("phone_number", "password1", "password2")

class LoginForm(forms.Form):
    phone_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)