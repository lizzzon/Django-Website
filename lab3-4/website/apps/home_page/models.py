from django.db import models
from django.urls import reverse


class Planet(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField(blank=True)
    photo = models.ImageField()
    author = models.CharField(max_length=30, default='Guest')
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.title