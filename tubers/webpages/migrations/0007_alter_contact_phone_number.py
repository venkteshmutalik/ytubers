# Generated by Django 4.1 on 2022-11-22 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
    ]
