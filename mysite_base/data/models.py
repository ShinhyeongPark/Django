from django.db import models

# Create your models here.
class IT(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    preview = models.CharField(max_length=200)
    crawled_time = models.CharField(max_length=200)

class ECO(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    preview = models.CharField(max_length=200)
    crawled_time = models.CharField(max_length=200)

class SPORTS(models.Model):
    title = models.CharField(max_length=200)
    preview = models.CharField(max_length=200)
    crawled_time = models.CharField(max_length=200)