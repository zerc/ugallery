# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='short_description',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='gallerymultiupload',
            name='short_description',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
