from django import forms
from .models import Contribution, Dataset

class DatasetCreationForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ['name', 'description', 'columns', 'data']
    
    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(DatasetCreationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(DatasetCreationForm, self).save(commit=False)
        inst.owner = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst

    
    

class ContributionForm(forms.ModelForm):

    class Meta:
        model = Contribution
        fields = ['textinput', 'intinput']

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        self._dataset = kwargs.pop('dataset')
        super(ContributionForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(ContributionForm, self).save(commit=False)
        inst.sender = self._user
        inst.dataset = self._dataset
        if commit:
            inst.save()
            self.save_m2m()
        return inst