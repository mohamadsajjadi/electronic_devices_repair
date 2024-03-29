from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import MyUserCreationForm, LoginForm, MyUserUpdateForm, ChangePasswordForm
from .models import MyUser

# Create your views here.

@login_required
def home_page(request):
    return render(request, 'home.html', {})

def register(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyUserCreationForm()

    return render(request, 'accounts/register.html', {'form' : form})

def login_user(request):
    # TODO : prevent user from entering
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['phone_number'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse_lazy('home'))
                return HttpResponse("Account Disabeled")
            return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {})

@login_required
def change_passsword(request):
    user_obj = get_object_or_404(MyUser, pk=request.user.id)
    form = ChangePasswordForm()
    message = None

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user_auth = authenticate(request, username=user_obj.phone_number, password=cd['old_password'])
            if user_obj and user_auth:
                user_obj.set_password(cd['new_password'])
                return redirect(reverse_lazy('accounts:profile'))
            else:
                message = 'old password is not correct'
            

    return render(request, 'accounts/update.html', {'form' : form, 'meesage':message})

@login_required
def update_user_data(request):
    user_obj = get_object_or_404(MyUser, pk=request.user.id)
    
    form = MyUserUpdateForm(instance=user_obj)
    if request.method == 'POST':
        form = MyUserUpdateForm(request.POST or None, instance=user_obj)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('accounts:profile'))
        
    return render(request, 'accounts/update.html', {'form' : form})

@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse_lazy("accounts:login"))