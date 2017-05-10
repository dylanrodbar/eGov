# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appeGov', '0003_auto_20170427_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=500, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('path', models.CharField(blank=True, db_column='Path', max_length=100, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'image',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=50, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=200, null=True)),
                ('content', models.CharField(blank=True, db_column='Content', max_length=5000, null=True)),
                ('views', models.IntegerField(blank=True, db_column='Views', null=True)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='Profilepicture',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('path', models.CharField(blank=True, db_column='Path', max_length=100, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'profilepicture',
            },
        ),
        migrations.CreateModel(
            name='Stadistic',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('yes', models.IntegerField(blank=True, db_column='Yes', null=True)),
                ('no', models.IntegerField(blank=True, db_column='No', null=True)),
                ('unknown', models.IntegerField(blank=True, db_column='Unknown', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'stadistic',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('tag', models.CharField(blank=True, db_column='Tag', max_length=20, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='Tagsxpost',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'tagsxpost',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=75, null=True)),
                ('username', models.CharField(blank=True, db_column='UserName', max_length=25, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=75, null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=200, null=True)),
                ('points', models.IntegerField(blank=True, db_column='Points', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Usertype',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'usertype',
            },
        ),
        migrations.CreateModel(
            name='Lawproject',
            fields=[
                ('fk_post', models.ForeignKey(db_column='FK_Post', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='appeGov.Post')),
                ('link', models.CharField(blank=True, db_column='Link', max_length=200, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'lawproject',
            },
        ),
    ]