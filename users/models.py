from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    username = models.EmailField(max_length=255, blank=False, unique=True)
    picture = models.URLField(max_length=200, blank=True)
