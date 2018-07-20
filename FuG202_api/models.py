from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    timespans = models.CharField(max_length=200)

class Genre(models.Model):
    name = models.CharField(max_length=20)
    restaurant_id = models.IntegerField()