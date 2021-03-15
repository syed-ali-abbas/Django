from django.db import models


class Hacker(models.Model):
    hacker_image= models.ImageField(upload_to='images/',blank=True)
    hacker_name = models.CharField(max_length=200)
    hacker_description = models.TextField()

    def __str__(self):
        return self.hacker_name
