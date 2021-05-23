from django.db import models

# Create your models here.

class Titulo_Judicial(models.Model):
    idTitulo_Judicial = models.AutoField(primary_key= True)
    numero= models.IntegerField(max_length=30)
    fecha_providencia= models.DateField()
    demandante= models.CharField(max_length=50)
    demandado= models.CharField(max_length=50)
    valor_titulo = models.IntegerField(max_length=20)
    num_oficio = models.IntegerField(max_length=30)
    num_rad_proceso= models.IntegerField(max_length=30)