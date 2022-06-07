from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Planet(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    context = models.TextField(blank=True)
    # photo = models.ImageField()
    author = models.CharField(max_length=30, default='Guest')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['author']