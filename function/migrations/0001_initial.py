# Generated by Django 4.0.4 on 2022-04-29 06:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formsubmit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=1000)),
                ('location', models.CharField(max_length=100)),
                ('journeyname', models.TextField(max_length=20)),
                ('date', models.DateField(verbose_name=datetime.datetime.now)),
            ],
        ),
    ]
