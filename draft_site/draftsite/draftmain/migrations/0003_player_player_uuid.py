# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 07:23
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('draftmain', '0002_auto_20170617_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]