# Generated by Django 3.1.2 on 2021-10-31 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20211031_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='is_main',
        ),
        migrations.AddField(
            model_name='articletags',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
