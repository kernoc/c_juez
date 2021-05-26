from django.db import models

# Create your models here.

class Person(models.Model):
    idPerson = models.AutoField(primary_key= True)
    identificationnumber = models.IntegerField(12)
    idtype= models.CharField(max_length=3)
    gender= models.CharField(max_length=3)
    name1= models.CharField(max_length=30)
    name2= models.CharField(max_length=30)
    surname1= models.CharField(max_length=30)
    surname2= models.CharField(max_length=30)
    residenceaddress= models.CharField(max_length=150)
    emaile= models.EmailField(max_length=150)
    countryorigin= models.CharField(max_length=70)
    cityorigin= models.CharField(max_length=100)
    role= models.CharField(max_length=70)
