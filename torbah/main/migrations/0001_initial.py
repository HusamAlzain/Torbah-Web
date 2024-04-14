# Generated by Django 5.0.3 on 2024-03-30 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('irrigated', models.BooleanField(default=False)),
                ('moisture_level', models.FloatField(blank=True, null=True)),
                ('plant_type', models.CharField(max_length=255)),
                ('soil_type', models.CharField(max_length=255)),
                ('area', models.FloatField()),
                ('location', models.CharField(max_length=255)),
                ('water_consumption', models.FloatField(blank=True, null=True)),
                ('irrigation_frequency', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]