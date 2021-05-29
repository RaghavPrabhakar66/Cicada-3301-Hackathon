from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def home(request):
    return render(request,'users/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signIn.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def stars(request):
    return render(request, 'users/starred.html')

def contributions(request):
    return render(request, 'users/myContri.html')

def leaderboard(request):
    
    return render(request, 'users/leaderboard.html')