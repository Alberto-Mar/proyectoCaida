from faker import Faker
from django.utils import timezone
from datetime import timedelta

from users.models import Hermano
from eventos.models import Acto
import random

fake = Faker("es_ES")
tipos_hermano = ['Costalero', 'Nazareno', 'Tambor', 'Protector']

def generar_hermanos(n):
    for _ in range(n):
        Hermano.objects.create(
            username=fake.user_name(),
            nombre=fake.first_name(),
            apellido1=fake.last_name(),
            apellido2=fake.last_name(),
            numero_hermano=random.unique.randint(1, 10000),
            dni=fake.unique.nif(),
            fec_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=80),
            cargo_junta=random.choice([True, False]),   
            email=fake.unique.email(),
        )

fechas = [
    timezone.now() - timedelta(days=random.randint(1, 3650))
    for _ in range(100)
]         
def generar_actos(n):
    for _ in range(n):
        Acto.objects.create(
            nombre=fake.sentence(nb_words=4),
            tipo=fake.word(),
            fec_inicio=random.choice(fechas),
        )