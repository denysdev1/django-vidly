# Generated by Django 5.1.4 on 2024-12-25 13:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]