from django.db import models

# Create your models here.

class Systemuser(models.Model):
    idSystemuser= models.AutoField(primary_key= True)
    user= models.CharField(max_length=10)
    password= models.CharField(max_length=10)
    idnumber = models.IntegerField(12)