from django.db import models
# Create your models here.

class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, null=True, blank=False)
    descripcion = models.TextField(max_length=200, null=True, blank=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="media/noticias", null=True, blank=True, default="media/default.jpg")
    
    def __str__(self):
        return self.titulo

class FotoGaleria(models.Model):
    id_foto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, null=True, blank=False)
    descripcion = models.CharField(max_length=200, null=True, blank=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="media/galeria", null=False, blank=False)
    
    def __str__(self):
        return self.titulo
    