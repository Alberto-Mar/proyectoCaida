from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.timezone import now

class TipoHermano(models.TextChoices):
    COSTALERO = 'Costalero', 'Costalero'
    NAZARENO = 'Nazareno', 'Nazareno'
    TAMBOR = 'Tambor', 'Tambor'
    PROTECTOR = 'Protector', 'Protector'
    
class RolReservado(models.Model):
    hermano = models.ForeignKey('Hermano', on_delete=models.CASCADE)
    rol = models.ForeignKey('eventos.Rol', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('hermano', 'rol')
        db_table = 'rol_reservado'

class HermanoManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Ha de proporcionar un email válido")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        
        if not password and 'dni' in extra_fields:
            password = extra_fields['dni']
            
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if password is None:
            raise ValueError("El superusuario debe tener contraseña explícita")

        return self.create_user(email, password, **extra_fields)

        

class Hermano(AbstractBaseUser, PermissionsMixin):    
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido1 = models.CharField(max_length=100, null=True, blank=True)
    apellido2 = models.CharField(max_length=100, null=True, blank=True)
    numero_hermano = models.IntegerField(unique=True)
    dni = models.CharField(max_length=20, unique=True)
    fec_nacimiento = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to="hermanos/", null=True, blank=True)
    cargo_junta = models.BooleanField(default=False)
    
    # Campos técnicos para Django Auth
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    tipo_hermano = models.CharField(
        max_length=20,
        choices=TipoHermano.choices,
        default=TipoHermano.PROTECTOR,
        blank=True,
    )
    
    roles = models.ManyToManyField(
        'eventos.Rol',
        through='RolReservado',
        blank=True,
    )
    
    objects = HermanoManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["numero_hermano", "nombre", "dni"]
    
    def save(self, *args, **kwargs):
        if not self.pk and not self.password:
            self.set_password(self.dni)
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.email} - {self.nombre} {self.apellido1}"
