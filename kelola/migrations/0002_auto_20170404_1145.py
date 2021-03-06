# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-04 04:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kelola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BabyBio',
            fields=[
                ('id_baby', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('baby_name', models.CharField(max_length=100)),
                ('date_birth', models.DateField(blank=True, null=True)),
                ('address', models.TextField()),
                ('mother_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('weight_birth', models.IntegerField()),
                ('height_birth', models.IntegerField()),
                ('headcircumference_birth', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('babyname', models.CharField(max_length=50)),
                ('check', models.CharField(choices=[('weight', 'Weight'), ('height', 'Height'), ('headcircumference', 'HeadCircumference'), ('immunization', 'Immunization')], max_length=30)),
                ('value', models.IntegerField()),
                ('imun_value', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Health', 'health'), ('Growing', 'growing'), ('Development', 'development'), ('Immunization', 'immunization')], max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
