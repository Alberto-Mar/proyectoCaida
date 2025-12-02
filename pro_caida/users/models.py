from django.db import models
from django.utils.timezone import now

class Hermano(models.Model):
    id_hermano = models.AutoField(primary_key=True)
    numero_hermano = models.IntegerField(unique=True)
    nombre_completo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    fec_nacimiento = models.DateField()
    foto = models.ImageField(upload_to="hermanos/", null=True, blank=True)
    cargo_junta = models.CharField(max_length=150, null=True, blank=True)
#     id_tipo_hermano = models.ForeignKey(
#         TipoHermano, on_delete=models.CASCADE
#  )
    
class TipoHermano(models.Model):
    id_tipo_hermano = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)