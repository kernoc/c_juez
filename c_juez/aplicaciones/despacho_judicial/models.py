from django.db import models

# Create your models here.

class Despacho_Judicial(models.Model):
    idDespacho_Judicial = models.AutoField(primary_key= True)
    nomb_despacho= models.CharField(max_length=150)
    nomb_juez= models.CharField(max_length=150)
    direccion= models.CharField(max_length=150)
    correo_e= models.EmailField(max_length=150)
    pais= models.CharField(max_length=70)
    ciudad= models.CharField(max_length=100)
    telefono= models.IntegerField(max_length=70)