from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import MyUser

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = "__all__"

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['phone_number', 'email', 'first_name', 'last_name']
