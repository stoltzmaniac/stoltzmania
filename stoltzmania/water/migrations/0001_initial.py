# Generated by Django 4.0.10 on 2023-02-26 22:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurfaceWaterStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('div', models.IntegerField(null=True)),
                ('wd', models.IntegerField(null=True)),
                ('county', models.CharField(max_length=500, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('station_name', models.CharField(max_length=500, null=True)),
                ('dwr_abbrev', models.CharField(max_length=50, null=True)),
                ('usgs_station_id', models.IntegerField(null=True)),
                ('data_source', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('por_start', models.IntegerField(null=True)),
                ('por_end', models.IntegerField(null=True)),
                ('utm_x', models.IntegerField(null=True)),
                ('utm_y', models.IntegerField(null=True)),
                ('location_accuracy', models.CharField(max_length=500, null=True)),
                ('more_information', models.CharField(max_length=500, null=True)),
                ('location', models.CharField(max_length=500, null=True)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
            ],
        ),
    ]