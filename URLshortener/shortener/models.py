from django.db import models
from django.contrib.auth.models import User

class UrlShortener(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.original_url


