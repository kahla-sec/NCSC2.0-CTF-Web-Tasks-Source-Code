from django.db import models


class Shinobi(models.Model):
    picture = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)



