# Generated by Django 5.0.6 on 2024-07-05 09:52

import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequencer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('sequencer', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(default=dict), size=None)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sequencer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
