from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    published_on = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', default='default_image.jpg')

    def __str__(self):
        return self.title
    
    def publish(self):
        self.published_on = timezone.now()
        self.save()
    
class PhotoGallery(models.Model):
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/')

    def publish(self):
        self.publish_on = timezone.now()
        self.save()

    def __str__(self):
        return self.description

