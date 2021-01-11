from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

class Employer(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    field = models.ManyToManyField(Category) 
    thumbnail = models.ImageField()
    description = models.CharField(max_length=5000)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Job(models.Model):
    JOB_TYPE = (
        ('full', 'Full Time'),
        ('part', 'Part Time'),
        ('internship', 'Internship'),
        ('temporary', 'Temporary')
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    description = models.CharField(max_length=4000)
    job_type = models.CharField(choices=JOB_TYPE, max_length=20)
    listed_on = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    slots = models.FloatField(default=1)
    support_contact = models.CharField(help_text='Support phone number', blank=True, max_length=20)

    def __str__(self):
        return self.title
