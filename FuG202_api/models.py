from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return 'Tag[id: {id}, text: {text}]'.format(id=self.id, text=self.tag_name)


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    timespans = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, related_name='restaurants')
