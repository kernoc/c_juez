from django.db import models

# Create your models here.

class Judicialtitle(models.Model):
    idJudicialtitle = models.AutoField(primary_key= True)
    number= models.IntegerField(30)
    providencedate= models.DateField()
    applicant= models.CharField(max_length=50)
    defendant= models.CharField(max_length=50)
    titlevalue = models.IntegerField(20)
    tradenumber = models.IntegerField(30)
    processfilingnumber= models.IntegerField(30)