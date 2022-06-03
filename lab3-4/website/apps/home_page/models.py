from django.db import models


class Planet(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    # photo = models.ImageField(upload_to="images/%Y/")
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title