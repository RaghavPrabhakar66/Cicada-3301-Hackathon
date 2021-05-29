from django.shortcuts import redirect, render, get_object_or_404
from .models import Dataset
import os
from .forms import DatasetCreationForm, ContributionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def datasets(request):
    datasets = Dataset.objects.all().order_by('-stars')
    return render(request, 'dataset.html', {'datasets': datasets})


@login_required
def createDataset(request):
    if request.method=='POST':
        form = DatasetCreationForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your dataset has been created!')
            return redirect('home')
    else:
        form = DatasetCreationForm(user=request.user)
        
    return render(request, 'createDataset.html', {'form': form})


def explore(request, dataset_id):
    dataset = get_object_or_404(Dataset, pk=dataset_id)
    return render(request, 'explore.html', {'dataset': dataset})


def contribute(request, dataset_id):
    if request.method=='POST':
        form = ContributionForm(request.POST, user=request.user, dataset = Dataset.objects.get(id=dataset_id))
        if form.is_valid():
            form.save()
            messages.success(request, f'Your contribution has been given!')
            return redirect('home')
    else:
        form = ContributionForm(user=request.user, dataset = Dataset.objects.get(id=dataset_id))
        
    return render(request, 'contribute.html', {'form': form})
