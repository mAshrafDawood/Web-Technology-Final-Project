from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *

# Create your views here.

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('home')
        return render(request, 'user/profile.html', {'form': form})
    form = PasswordChangeForm(request.user)
    return render(request, 'user/profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1']
                                    )
            login(request, new_user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

def signin(request):
    return render(request, 'user/signin.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserForm(instance=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
        return render(request, 'user/profile.html', {'form': form})
    form = UserForm(instance=request.user)
    return render(request, 'user/profile.html', {'form': form})