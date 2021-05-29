from django.shortcuts import redirect, render
# from .models import Dataset
from .DL.text import TextFilter
import os
from django.conf import settings
from pandas import DataFrame
# from .forms import DatasetCreationForm
from django.contrib import messages


# Create your views here.
def datasets(request):
    datasets = Dataset.objects.all().order_by('-stars')
    return render(request, 'dataset.html', {'datasets': datasets})

def createDataset(request):
    form = DatasetCreationForm(request.POST)
    if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('home')
    return render(request, 'createDataset.html')

# Return True if given text is spam
def checkSpam(path, text):
    filter = TextFilter()
    return filter.run(path, text)

# Genereate spam filter, given a list of texts
def makeFilter(column, path):
    df = DataFrame()
    df.read_csv(path)
    texts = df.iloc[column-1:column]
    filter = TextFilter()
    filter.generateFilter(path, texts)
    return

# Append given data in given csv file
def commitContribution(data, path='./storage/sentiment.csv'):
    df = DataFrame()
    df.read_csv(path)
    df.append(data)
    df.to_csv(path)