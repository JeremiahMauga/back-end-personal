# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import NullBooleanField

class Inventory(models.Model):
    game_title = models.CharField(max_length=100)
    voter = models.CharField(max_length=100)
    votes = models.IntegerField()

    def __str__(self):
        return f"Game Title: {self.game_title} Voter: {self.voter} Votes: {self.votes}"


