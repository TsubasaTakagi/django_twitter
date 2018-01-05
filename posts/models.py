from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    body = models.TextField(max_length=140)
    published = models.DateTimeField(default=timezone.now)
    image = models.ImageField()