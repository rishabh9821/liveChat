from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True)
    createDate = models.DateTimeField(default = timezone.now)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name = 'messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name = 'messages', on_delete=models.CASCADE)
    content = models.TextField()
    dateAdded = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ('-dateAdded',)