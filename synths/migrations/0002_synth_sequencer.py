# Generated by Django 5.0.6 on 2024-07-09 09:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='synth',
            name='sequencer',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(default=dict), blank=True, null=True, size=None),
        ),
    ]
