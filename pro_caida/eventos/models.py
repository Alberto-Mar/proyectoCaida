from django.db import models
from users.models import Hermano
# Create your models here.
class Acto(models.Model):
    id_acto = models.AutoField(primary_key=True)
    fec_inicio = models.DateTimeField()
    nombre = models.CharField(max_length=150, unique=True)
    tipo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="actos/", null=True, blank=True)
    id_hermano = models.ForeignKey(
        Hermano, on_delete=models.SET_NULL, null=True, blank=True
    )
    
    def __str__(self):
        return f"{self.nombre}"
    
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=False, blank=False)
    protocolo = models.TextField(null=True, blank=True)
    aforo = models.IntegerField(null=True, blank=True)
    limite = models.BooleanField(default=False)
    id_acto = models.ForeignKey(
        Acto, on_delete=models.CASCADE, null=False
    )
    
    def __str__(self):
        return f"{self.nombre} - {self.id_acto.nombre}"