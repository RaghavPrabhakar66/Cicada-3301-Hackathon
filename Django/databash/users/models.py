from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from datasets.models import Dataset, Contribution


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    github = models.URLField(max_length=500, blank=True)
    xp = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    stars = models.ManyToManyField(Dataset)
    contributions = models.ManyToManyField(Contribution)
