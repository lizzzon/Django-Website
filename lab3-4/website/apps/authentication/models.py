from django.db import models


class Task(models.Model):
    task = models.TextField('/')

    def __str__(self):
        return self.title