from django import forms
from .models import Contribution, Dataset

class DatasetCreationForm(forms.Form):
    class Meta:
        model = Dataset
        fields = ['name', 'description', 'columns', 'data']
    

class ContributionForm(forms.Form):

    class Meta:
        model = Contribution
        fields = ['textInput', 'intInput']