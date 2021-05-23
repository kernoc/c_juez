from django.db import models

# Create your models here.

class Libro(models.Model):
    idLibro = models.AutoField(primary_key= True)
    idPersona = models.ForeignKey(Persona)
    titulo= models.CharField(max_length=30)
    fecha= models.DateField()
    radicado = models.IntegerField(max_length=20)
    ingreso= models.FloatField()
    salida= models.FloatField()
    saldo_libro= models.FloatField()
    observaciones= models.CharField(max_length=50)