from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250)

    def summary(self):
        return self.title[:100]

    def __str__(self):
        return self.title
