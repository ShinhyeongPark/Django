from django.db import models
import datetime
# Create your models here.
class IT(models.Model):
    title = models.CharField(max_length=200,null=True)
    writer = models.CharField(max_length=200,null=True)
    preview = models.CharField(max_length=200,null=True)
    crawled_time = models.CharField(max_length=200 ,null=True)

    def __str__(self):
        return self.title

class ECO(models.Model):
    title = models.CharField(max_length=200,null=True)
    writer = models.CharField(max_length=200,null=True)
    preview = models.CharField(max_length=200,null=True)
    crawled_time = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title


class SPORTS(models.Model):
    title = models.CharField(max_length=200,null=True)
    preview = models.CharField(max_length=200,null=True)
    crawled_time = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title

class ALL(models.Model):
    title = models.CharField(max_length=200,null=True)
    preview = models.CharField(max_length=200,null=True)
    crawled_time = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title