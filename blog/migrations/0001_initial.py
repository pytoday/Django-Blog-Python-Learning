# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 04:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import redactor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, help_text='Upload your photo for Avatar', null=True, upload_to='gallery/avatar/%Y/%m/%d')),
                ('about', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Authors',
                'verbose_name': 'Detail Author',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', redactor.fields.RedactorField()),
                ('publish', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_page', to='blog.Author')),
            ],
            options={
                'verbose_name_plural': 'Pages',
                'ordering': ['-created'],
                'verbose_name': 'Detail Page',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='gallery/covers/%Y/%m/%d')),
                ('description', redactor.fields.RedactorField()),
                ('keywords', models.CharField(blank=True, help_text='Keywords sparate by comma.', max_length=200, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('publish', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_post', to='blog.Author')),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'ordering': ['-created'],
                'verbose_name': 'Detail Post',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'verbose_name': 'Detail Tag',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]