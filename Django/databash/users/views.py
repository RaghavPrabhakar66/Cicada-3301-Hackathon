from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.conf import settings
from django.contrib.auth import get_user_model
from datasets.models import Dataset


def home(request):
    datasets = Dataset.objects.all().order_by('-stars')[:5]
    user = get_user_model()
    leaders = user.objects.all().order_by('-xp')[:5]
    return render(request,'users/home.html', {'leaders': leaders, 'datasets': datasets})


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signIn.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def stars(request):
    current_user = request.user
    return render(request, 'users/starred.html', {'current_user': current_user})

def contributions(request):
    return render(request, 'users/myContri.html')

def leaderboard(request):
    datasets = Dataset.objects.all().order_by('-stars')
    user = get_user_model()
    leaders = user.objects.all().order_by('-xp')
    return render(request, 'users/leaderboard.html', {'leaders': leaders, 'datasets': datasets})

def mycontris(request):
    current_user = request.user
    datasets = current_user.contributions.dataset
    return render(request, 'myContri.html', {'datasets': datasets})