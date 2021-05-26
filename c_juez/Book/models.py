from django.db import models

# Create your models here.

class Book(models.Model):
    idBook = models.AutoField(primary_key= True)
    title= models.CharField(max_length=30)
    datei= models.DateField()
    settled= models.IntegerField(20)
    input= models.FloatField()
    output= models.FloatField()
    balancebook= models.FloatField()
    observations= models.CharField(max_length=50)