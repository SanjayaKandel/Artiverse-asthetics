from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def auth_view(request):
    register_form = CreateUserForm()
    login_form = LoginForm()

    if request.method == "POST":
        if 'register' in request.POST:
            register_form = CreateUserForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                return redirect('login')
        elif 'login' in request.POST:
            login_form = LoginForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')

    context = {'registerform': register_form, 'loginform': login_form}
    return render(request, 'User/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('/')
