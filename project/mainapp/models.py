from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=155)
    users = models.ManyToManyField(User,null=True ,blank=True, related_name='liked_rooms')

class Post(models.Model):
    description = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


