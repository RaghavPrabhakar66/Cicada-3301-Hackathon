from django.db import models
from django.conf import settings
from django import forms

# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    columns = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')))
    data = models.FileField()
    description = models.TextField(max_length=5000)
    stars = models.IntegerField(default=0)

class Attribute(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    datatype = models.CharField(max_length=200)



# Forms
class DatasetForm(forms.ModelForm):
    name = models.CharField(max_length=200, null=True, blank=True)
    columns = models.IntegerField() # add validator limit 10
    description = models.TextField(max_length=5000)


class DataForm(forms.ModelForm):
    def __init__(self, columns):
        super.__init__(self)
        for i in range(columns):
            self.fields['name' + str(i)] = models.CharField(max_length=200)
            self.fields['datatype' + str(i)] = models.CharField(choices=['image', 'text', 'integer'])

    def save(self, columns, dataset):
        for i in range(columns):
            Attribute.objects.create(
                dataset=dataset,
                name=self.fields['name' + str(i)],
                datatype=self.fields['datatype' + str(i)]
            )
