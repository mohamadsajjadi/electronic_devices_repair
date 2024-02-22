from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import MyUserCreationForm, LoginForm, MyUserUpdateForm
from .models import MyUser

# Create your views here.

@login_required
def home_page(request):
    return HttpResponse("you're fucking home page")

def register(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
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
    return HttpResponse("you're fucking profile")

@login_required
def change_passsword(request):
    return HttpResponse("you can change your password here")

@login_required
def update_user_data(request, user_id):
    print(user_id)
    user_obj = get_object_or_404(MyUser, pk=user_id)
    
    if user_obj.id != request.user.id:
        return HttpResponse('Forbbiden request')


    form = MyUserUpdateForm(instance=user_obj)
    if request.method == 'POST':
        form = MyUserUpdateForm(request.POST or None, instance=user_obj)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('profile'))
        
    
    return render(request, 'accounts/update.html', {'form' : form})