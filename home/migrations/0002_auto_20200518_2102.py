# Generated by Django 2.2 on 2020-05-18 19:02

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]