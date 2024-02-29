from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
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

class MyUserUpdateForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['role', 'email', 'first_name', 'last_name']

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='current password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='new password', widget=forms.PasswordInput)
    new_password_confirm = forms.CharField(label='new password confirm', widget=forms.PasswordInput)
    
    def clean(self):
        cd = self.cleaned_data
        if cd['new_password'] != cd['new_password_confirm']:
            raise ValidationError('password are not the same')
        return cd
        