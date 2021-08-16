# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import NullBooleanField

class Inventory(models.Model):
    game_title = models.CharField(max_length=100)
    voters = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name="inventory", on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user} Game Title: {self.game_title}"


