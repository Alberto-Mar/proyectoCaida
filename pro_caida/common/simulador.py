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
            nombre_completo=fake.name(),
            numero_hermano=random.unique.randint(10, 9999),
            dni=fake.unique.nif(),
            fec_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=80),
            cargo_junta=fake.boolean(chance_of_getting_true=5),
            tipo_hermano=random.choice(tipos_hermano),
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