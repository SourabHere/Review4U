import email
from django.db import models

# Create your models here.
class gamesrev(models.Model):
    games_id=models.AutoField(primary_key=True)
    game_name=models.CharField(max_length=100)
    email=models.CharField(max_length=150,default="")
    release_date=models.DateField()
    rating=models.IntegerField(default=0)
    desc=models.CharField(max_length=2000,default="")
    noOfRev=models.IntegerField(default=1)
    game_img=models.ImageField(upload_to="games/images",default="")

    def __str__(self):
        return self.game_name

class myrev(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    game_name=models.CharField(max_length=150,default="")
    email=models.CharField(max_length=150)
    rating=models.IntegerField(default=0)

    def __str__(self):
        return self.game_name
        
class contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)    
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=25)
    desc=models.CharField(max_length=2000,default="")

    def __str__(self):
        return self.name
