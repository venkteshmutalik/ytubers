# Generated by Django 4.1 on 2022-11-22 08:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0011_alter_youtuber_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 22, 13, 47, 26, 833013)),
        ),
    ]