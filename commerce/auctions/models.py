from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class create_listing(models.Model):
    title = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=128, blank=True)
    starting_bid = models.IntegerField(blank=True)
    image = models.ImageField(blank=True)
    Category = models.CharField(max_length=64, blank=True)


    def __str__(self):
        return f"{self.id} : {self.title} , {self.description}, {self.starting_bid}, {self.Category}, {self.image}"