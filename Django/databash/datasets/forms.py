from django import forms
from .models import Dataset

class DatasetCreationForm(forms.Form):
    class Meta:
        model = Dataset
        fields = ['name', 'description', 'columns']