from django.db import models

# Create your models here.

class Judicialoffice(models.Model):
    idJudicialoffice = models.AutoField(primary_key= True)
    nameoffice= models.CharField(max_length=150)
    namejudge= models.CharField(max_length=150)
    address= models.CharField(max_length=150)
    emaile= models.EmailField(max_length=150)
    country= models.CharField(max_length=70)
    city= models.CharField(max_length=100)
    phone= models.IntegerField(70)