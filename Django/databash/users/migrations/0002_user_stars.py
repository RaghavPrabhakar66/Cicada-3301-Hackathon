# Generated by Django 3.2.3 on 2021-05-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0006_auto_20210529_0949'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stars',
            field=models.ManyToManyField(to='datasets.Dataset'),
        ),
    ]
