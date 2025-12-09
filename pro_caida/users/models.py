from django.db import models
from django.utils.timezone import now

class TipoHermano(models.Model):
    Costalero = 'Costalero'
    Nazareno = 'Nazareno'
    Tambor = 'Tambor'
    Protector = 'Protector'
    
    
class Hermano(models.Model):
    id_hermano = models.AutoField(primary_key=True)
    numero_hermano = models.IntegerField(unique=True)
    nombre_completo = models.CharField(max_length=200)
    dni = models.CharField(max_length=20, unique=True)
    fec_nacimiento = models.DateField()
    foto = models.ImageField(upload_to="hermanos/", null=True, blank=True)
    cargo_junta = models.BooleanField(default=False)
    tipo_hermano = models.CharField(
        choices=[
            (TipoHermano.Costalero, 'Costalero'),
            (TipoHermano.Nazareno, 'Nazareno'),
            (TipoHermano.Tambor, 'Tambor'),
            (TipoHermano.Protector, 'Protector'),
        ],
        default=TipoHermano.Protector,
    )
    
    roles = models.ManyToManyField(
        'eventos.Rol',
        through='RolReservado',
        blank=True,
    )
    
    def __str__(self):
        return f"{self.numero_hermano} - {self.nombre_completo}"

class RolReservado(models.Model):
    hermano = models.ForeignKey('Hermano', on_delete=models.CASCADE)
    rol = models.ForeignKey('eventos.Rol', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('hermano', 'rol')
        db_table = 'rol_reservado'
    
    
