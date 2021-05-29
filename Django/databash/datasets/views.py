from django.shortcuts import render
from .models import Dataset
from rest_framework import serializers, status
from .models import Dataset
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import DatasetSerializers

# Create your views here.
def datasets(request):
    datasets = Dataset.objects.all().order_by('-stars')
    return render(request, 'dataset.html', {'datasets': datasets})


class DatasetView(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializers
    

@api_view(["POST"])
def checkSpam(request):
    try:
        #text = 
        pass
        
    except ValueError as error:
        return Response(error.args[0], status.HTTP_400_BAD_REQUEST)