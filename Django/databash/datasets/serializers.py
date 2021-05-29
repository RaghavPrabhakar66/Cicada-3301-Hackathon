from os import error
from rest_framework import serializers, status
from .models import Dataset
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response

class DatasetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ('text', 'integer')


