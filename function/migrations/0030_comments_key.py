# Generated by Django 4.0.4 on 2022-05-05 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('function', '0029_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='key',
            field=models.IntegerField(default=0),
        ),
    ]
