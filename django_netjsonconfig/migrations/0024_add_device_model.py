# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-27 10:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import re
import uuid

from django_netjsonconfig.utils import get_random_key


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0023_template_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('mac_address', models.CharField(help_text='primary mac address', max_length=17, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', 32), code='invalid', message='Must be a valid mac address.')])),
                ('key', models.CharField(db_index=True, default=get_random_key, help_text='unique device key', max_length=64, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[^\\s/\\.]+$', 32), code='invalid', message='Key must not contain spaces, dots or slashes.')])),
                ('model', models.CharField(blank=True, help_text='device model and manufacturer', max_length=64)),
                ('os', models.CharField(blank=True, help_text='operating system identifier', max_length=128, verbose_name='operating system')),
                ('notes', models.TextField(blank=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='config',
            name='device',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_netjsonconfig.Device'),
        ),
    ]
