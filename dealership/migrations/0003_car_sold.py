# Generated by Django 4.2.2 on 2023-10-23 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealership', '0002_alter_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
