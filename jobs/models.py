from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
