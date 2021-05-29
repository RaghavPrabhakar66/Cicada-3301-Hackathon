from django.db import models
from django.conf import settings
from django import forms

# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data = models.FileField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    integer = models.IntegerField(blank=True, null=True)
    columns = models.IntegerField(choices=[(3, 3)])
    spam = models.BooleanField(default=False)
    # selected = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=5000)
    stars = models.IntegerField(default=0)

class Attribute(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    datatype = models.CharField(max_length=200)

# class column_2(models.Model):
#     c1 = models.CharField(max_length=200, null=True, blank=True)
#     c2 = models.CharField(max_length=200, null=True, blank=True)
#     datatype_c1 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c2 = models.CharField(choices=['image', 'text', 'integer'])

class column_3(forms.ModelForm):
    c1 = models.CharField(max_length=200, null=True, blank=True)
    c2 = models.CharField(max_length=200, null=True, blank=True)
    c3 = models.CharField(max_length=200, null=True, blank=True)
    datatype_c1 = models.CharField(choices=(('image', 'image'), ('text', 'text'), ('integer', 'integer')))
    datatype_c2 = models.CharField(choices=(('image', 'image'), ('text', 'text'), ('integer', 'integer')))
    datatype_c3 = models.CharField(choices=(('image', 'image'), ('text', 'text'), ('integer', 'integer')))

# class column_4(models.Model):
#     c1 = models.CharField(max_length=200, null=True, blank=True)
#     c2 = models.CharField(max_length=200, null=True, blank=True)
#     c3 = models.CharField(max_length=200, null=True, blank=True)
#     c4 = models.CharField(max_length=200, null=True, blank=True)
#     datatype_c4 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c1 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c2 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c3 = models.CharField(choices=['image', 'text', 'integer'])  

# class column_5(models.Model):
#     c1 = models.CharField(max_length=200, null=True, blank=True)
#     c2 = models.CharField(max_length=200, null=True, blank=True)
#     c3 = models.CharField(max_length=200, null=True, blank=True)
#     c4 = models.CharField(max_length=200, null=True, blank=True)
#     c5 = models.CharField(max_length=200, null=True, blank=True)
#     datatype_c5 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c4 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c1 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c2 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c3 = models.CharField(choices=['image', 'text', 'integer'])  

# class column_6(models.Model):
#     c1 = models.CharField(max_length=200, null=True, blank=True)
#     c2 = models.CharField(max_length=200, null=True, blank=True)
#     c3 = models.CharField(max_length=200, null=True, blank=True)
#     c4 = models.CharField(max_length=200, null=True, blank=True)
#     c5 = models.CharField(max_length=200, null=True, blank=True)
#     c6 = models.CharField(max_length=200, null=True, blank=True)
#     datatype_c6 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c5 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c4 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c1 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c2 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c3 = models.CharField(choices=['image', 'text', 'integer']) 

# class column_7(models.Model):
#     c1 = models.CharField(max_length=200, null=True, blank=True)
#     c2 = models.CharField(max_length=200, null=True, blank=True)
#     c3 = models.CharField(max_length=200, null=True, blank=True)
#     c4 = models.CharField(max_length=200, null=True, blank=True)
#     c5 = models.CharField(max_length=200, null=True, blank=True)
#     c6 = models.CharField(max_length=200, null=True, blank=True)
#     c7 = models.CharField(max_length=200, null=True, blank=True)
#     datatype_c7 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c6 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c5 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c4 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c1 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c2 = models.CharField(choices=['image', 'text', 'integer'])
#     datatype_c3 = models.CharField(choices=['image', 'text', 'integer'])    


# # Forms
# class DatasetForm(forms.ModelForm):
#     name = models.CharField(max_length=200, null=True, blank=True)
#     columns = models.IntegerField() # add validator limit 10
#     description = models.TextField(max_length=5000)


# class DataForm(forms.ModelForm):
#     def __init__(self):
#         super.__init__(self)
        
#         for i in range(columns):
#             self.fields['name' + str(i)] = models.CharField(max_length=200)
#             self.fields['datatype' + str(i)] = models.CharField(choices=['image', 'text', 'integer'])

#     def save(self, columns, dataset):
#         for i in range(columns):
#             Attribute.objects.create(
#                 dataset=dataset,
#                 name=self.fields['name' + str(i)],
#                 datatype=self.fields['datatype' + str(i)]
#             )
