from django.shortcuts import render
from .models import Dataset

# Create your views here.
def datasets(request):
    datasets = Dataset.objects.all().order_by('-stars')
    return render(request, 'dataset.html', {'datasets': datasets})