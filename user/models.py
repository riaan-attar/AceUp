from django.db import models

# Create your models here.
class notes(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    subject = models.CharField(max_length=100)
    url = models.FileField(upload_to ='satic/notes/')

class testimonial(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='satic/photos')
    testi = models.TextField()
    git = models.URLField()
    linkdin = models.URLField()