# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-02 09:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_shortmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortmessage',
            name='ShortMessage_user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
