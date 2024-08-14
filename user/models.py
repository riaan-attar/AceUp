from django.db import models

# Create your models here.
class notes(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField(max=2)
    subject = models.CharField(max_length=100)
    url = models.URLField(max_length=2000)