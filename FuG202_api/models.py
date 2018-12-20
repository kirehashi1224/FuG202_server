from django.db import models


class PriceTag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return 'Price [id: {id}, text: {text}]'.format(id=self.id, text=self.name)


class GenreTag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return 'Genre [id: {id}, text: {text}]'.format(id=self.id, text=self.name)


class DistanceTag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return 'Distance [id: {id}, text: {text}]'.format(id=self.id, text=self.name)


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    timespans = models.CharField(max_length=400)
    image = models.CharField(max_length=200, null=True, blank=True)
    priceTags = models.ManyToManyField(PriceTag, related_name='restaurants')
    genreTags = models.ManyToManyField(GenreTag, related_name='restaurants')
    distanceTags = models.ManyToManyField(DistanceTag, related_name='restaurants')
