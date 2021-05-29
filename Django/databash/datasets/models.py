from django.db import models
from django.conf import settings
from django import forms
from django.db.models.signals import post_save
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
import os
from django.http import HttpResponse
import pandas as pd
from .DL.text import TextFilter
from django.urls import reverse



# Return True if given text is spam
def checkSpam(path, string):
    filter = TextFilter()
    return filter.run(path, string)

# Genereate spam filter, given a list of texts
def makeFilter(column, path):
    df = pd.read_csv(path)
    texts = df.iloc[column-1:column]
    filter = TextFilter()
    filter.generateFilter(path, texts)


# Append given data in given csv file
def commitContribution(data, path):
    print('cunts say hi from csv')
    with open(path, 'a') as f:
        f.write(f"\n\"{str(data[0])}\", {str(data[1])}\n")


# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data = models.FileField(blank=True, null=True)
    columns = models.IntegerField(choices=[(3,1),(3,2),(3, 3),(3,4),(3,5)])
    description = models.TextField(max_length=5000)
    stars = models.IntegerField(default=0)    

    def get_absolute_url(self):
        return reverse("explore", kwargs={"id": self.id})

class Attribute(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    datatype = models.CharField(max_length=200)

class Contribution(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    isSpam = models.BooleanField(default=False)
    textinput = models.CharField(max_length=1000)
    intinput = models.IntegerField(default=0)

# @receiver(post_save, sender=Dataset)
# def create_filter(sender, instance, created, *args, **kwargs):
#     if created:
#         makeFilter(column=1, path=os.path.join(settings.BASE_DIR, 'datasets/Storage/filter.npy'))

def user_contribution_counter(instance):
    print("hello there")
    instance.sender.contributions.add(instance)
    xp = instance.sender.xp
    xp += 100

def contri(sender, instance, *args, **kwargs):
    print("sexy sex sextime")
    spam = checkSpam(os.path.join(settings.BASE_DIR, 'datasets/Storage/filter.npy'), instance.textinput)
    if (spam):
        instance.isSpam = True
        print("penis very large: (It is spamu)")
        return HttpResponse("yayy it doesnt work")
    else:
        print("penis very small")
        # instance.save()
        commit_contri(instance)
        user_contribution_counter(instance)

post_save.connect(contri, sender=Contribution)    

def commit_contri(instance):
    print('cunts get their share')
    commitContribution([instance.textinput, instance.intinput], path=os.path.join(settings.BASE_DIR, 'datasets/Storage/sentiment.csv'))


class column_3(forms.ModelForm):
    c1 = models.CharField(max_length=200, null=True, blank=True)
    c2 = models.CharField(max_length=200, null=True, blank=True)
    c3 = models.CharField(max_length=200, null=True, blank=True)
    datatype_c1 = models.CharField(choices=(('image', 'image'), ('text', 'text'), ('integer', 'integer')))
    datatype_c2 = models.CharField(choices=(('image', 'image'), ('text', 'text'), ('integer', 'integer')))
    datatype_c3 = models.CharField(choices=(('image', 'image'), ('text', 'text'), ('integer', 'integer')))