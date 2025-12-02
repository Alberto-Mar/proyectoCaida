from django.db import models
# Create your models here.
class Acto(models.Model):
    id_acto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, unique=True, null=False, blank=False)
    fec_inicio = models.DateTimeField(null=False, blank=False)
    tipo = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(verbose_name='imagen', null=True, blank=True)
    # id_hermano = models.ForeignKey(
    #     Hermano, on_delete=models.SET_NULL, null=True, blank=True
    # )
    
    def __str__(self):
        return self.nombre