from django.db import models

# Create your models here.

class Usuario_Sistema(models.Model):
    idUsuario_Sistema= models.AutoField(primary_key= True)
    usuario= models.CharField(max_length=10)
    contraseña= models.CharField(max_length=10)
    num_identificacion = models.IntegerField(max_length=12)