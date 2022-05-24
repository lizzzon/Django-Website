from django.db import models


class Planet(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    # photo = models.ImageField(upload_to="static/website/images")
