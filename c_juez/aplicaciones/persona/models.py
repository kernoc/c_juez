from django.db import models

# Create your models here.

class Persona(models.Model):
    idPersona = models.AutoField(primary_key= True)
    num_identificacion = models.IntegerField(max_length=12)
    tipo_identificacion= models.CharField(max_length=3)
    sexo= models.CharField(max_length=3)
    nombre1= models.CharField(max_length=30)
    nombre2= models.CharField(max_length=30)
    apellido1= models.CharField(max_length=30)
    apellido2= models.CharField(max_length=30)
    dir_residencia= models.CharField(max_length=150)
    correo_e= models.EmailField(max_length=150)
    pais_origen= models.CharField(max_length=70)
    ciudad_origen= models.CharField(max_length=100)
    rol= models.CharField(max_length=70)
