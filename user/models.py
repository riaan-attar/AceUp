from django.db import models

# Create your models here.
class notes(models.Model):
    title = models.CharField(max_length=255)
    # unit =  models.IntegerField(null =True,blank =True)
    year = models.IntegerField()
    subject = models.CharField(max_length=100)
    url = models.FileField(upload_to ='satic/notes/')
    
class docs(models.Model):
    title = models.CharField(max_length=255)
    url = models.FileField(upload_to='satic/docs')

class testimonial(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='satic/photos')
    testi = models.TextField()
    git = models.URLField()
    linkdin = models.URLField()

class pyqs(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    subject = models.CharField(max_length=100)
    url = models.FileField(upload_to='satic/pyqs')
    exam = models.CharField(max_length=100)
class events(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(null = True,blank=True)
    time = models.TimeField(null = True,blank=True) 
    bd = models.CharField(max_length=1000)
    description = models.TextField(blank=True,null=True)
    thumbnail = models.FileField(upload_to='satic/event')

class event(models.Model):
    event = models.ForeignKey(events ,on_delete=models.CASCADE)
    photos = models.FileField(upload_to = 'satic/event')
    photoCaption = models.CharField(max_length= 300)
    url = models.URLField(blank =True,null = True )

class roadmaps(models.Model):
    title = models.CharField(max_length=255)
    url = models.FileField(upload_to='satic/roadmaps/')    
