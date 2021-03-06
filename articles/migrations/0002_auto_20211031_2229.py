# Generated by Django 3.1.2 on 2021-10-31 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='articles',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='scopes', through='articles.ArticleTags', to='articles.Tags', verbose_name='Тематики статьи'),
        ),
    ]
