# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comments_images_lawprojects_posts_profilepictures_stadistics_tags_users_usertypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pointspost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'pointspost',
            },
        ),
        migrations.CreateModel(
            name='Votespost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'votespost',
            },
        ),
    ]
