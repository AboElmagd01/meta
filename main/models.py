import json

from django.db import models

# Create your models here.

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,default="Room")
    type = models.CharField(max_length=200,default="Single")
    avaliable = models.BooleanField(default=True)
    src = models.CharField(max_length=600,default="Image")
    desc = models.CharField(max_length=600,default="A room")
    price = models.IntegerField(default=50)
    notavailable = models.CharField(default='TTTTTTT',max_length=8)
    def __str__(self):

        return self.title

class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="meal")
    desc = models.CharField(max_length=600,default="A dish")


    def __str__(self):
        return self.title


class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="meal")
    desc = models.CharField(max_length=600,default="A dish")
    terms1 = models.CharField(max_length=200,default="terms")
    terms2 = models.CharField(max_length=200,default="terms")
    terms3 = models.CharField(max_length=200,default="terms")
    terms4 = models.CharField(max_length=200,default="terms")
    src = models.CharField(max_length=600,default="Image")
    def __str__(self):
        return self.title



class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey("Room",on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    spot = models.DateField()
