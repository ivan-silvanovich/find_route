# Generated by Django 3.2.9 on 2021-12-27 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='train',
            options={'ordering': ['from_city', 'to_city'], 'verbose_name': 'Поезд', 'verbose_name_plural': 'Поезда'},
        ),
    ]
