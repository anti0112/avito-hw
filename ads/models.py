from django.db import models

class Ads(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    author = models.CharField(max_length=2000)
    price = models.IntegerField()
    description = models.TextField()
    address = models.TextField()
    is_published = models.BooleanField(default=False)

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    