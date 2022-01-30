from distutils.command.upload import upload
import email
from email.policy import default
from numbers import Rational
from os import name
from platform import release
from statistics import mode
from django.db import models

# Create your models here.
class animesrev(models.Model):
    anime_id=models.AutoField(primary_key=True)
    anime_name=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    release_date=models.DateField()
    rating=models.IntegerField(default=0)
    desc=models.CharField(max_length=2000)
    anime_img=models.ImageField(upload_to="animes/images",default="")
    noOfRev=models.IntegerField(default=1)

    def __str__(self):
        return self.anime_name

class contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150,default="")
    phone=models.CharField(max_length=15)
    desc=models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class myrev(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    anime_name=models.CharField(max_length=150,default="")
    email=models.CharField(max_length=150)
    rating=models.IntegerField(default=0)

    def __str__(self):
        return self.anime_name
        
