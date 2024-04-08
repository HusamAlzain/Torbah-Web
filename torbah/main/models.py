from django.db import models
from django.contrib.auth.models import User

class Sensor(models.Model):
    """
    Represents a sensor used for data collection on a farm.
    """
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    battery_life = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.type})"

class Farm(models.Model):
    """
    Represents a farm with its attributes.
    """
    name = models.CharField(max_length=255)
    soil_type = models.CharField(max_length=255)
    area = models.FloatField()
    water_source = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    sensors = models.ManyToManyField(Sensor)  # Farm has many Sensors (Many-to-Many relationship)

    def __str__(self):
        return self.name

class Plant(models.Model):
  """
  Represents a type of plant with its characteristics.
  """
  name = models.CharField(max_length=255)
  irrigated = models.BooleanField(default=False)
  moisture_level = models.FloatField(blank=True, null=True)
  plant_type = models.CharField(max_length=255)
  water_consumption = models.FloatField(blank=True, null=True)
  irrigation_frequency = models.IntegerField(blank=True, null=True)
  expected_yield = models.FloatField(blank=True, null=True)
  water_requirements = models.FloatField(blank=True, null=True)
  farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # One plant belongs to one farm

  def __str__(self):
    return self.name

