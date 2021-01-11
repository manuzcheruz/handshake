from django.db import models

# Create your models here.
class Center(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    location = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=5000)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.name
