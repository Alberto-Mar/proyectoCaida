import random
from faker import Faker
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import make_password
from users.models import Hermano
from eventos.models import Acto

fake = Faker("es_ES")

def generar_hermanos(n):
    hermanos_a_crear = []
    # Obtenemos el último número para no chocar si ya hay datos
    ultimo_h = Hermano.objects.order_by('-numero_hermano').first()
    start_num = (ultimo_h.numero_hermano + 1) if ultimo_h else 1
    
    print(f"Generando {n} hermanos en memoria...")
    
    for i in range(n):
        dni_fake = fake.unique.nif()
        email_fake = fake.unique.email()
        
        nuevo_hermano = Hermano(
            email=email_fake,
            username=fake.user_name(),
            nombre=fake.first_name(),
            apellido1=fake.last_name(),
            apellido2=fake.last_name(),
            numero_hermano=start_num + i,
            dni=dni_fake,
            # Seteamos el password directamente hasheado (DNI)
            password=make_password(dni_fake), 
            fec_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=80),
            cargo_junta=random.choice([True, False]),
            tipo_hermano=random.choice(['Costalero', 'Nazareno', 'Tambor', 'Protector']),
            is_active=True
        )
        hermanos_a_crear.append(nuevo_hermano)

    print("Insertando masivamente en Base de Datos...")
    Hermano.objects.bulk_create(hermanos_a_crear)
    print(f"Éxito: {n} hermanos creados.")

def generar_actos(n):
    actos_a_crear = []
    print(f"Generando {n} actos...")
    
    for _ in range(n):
        actos_a_crear.append(Acto(
            nombre=fake.sentence(nb_words=4),
            tipo=fake.word(),
            fec_inicio=timezone.now() - timedelta(days=random.randint(1, 365))
        ))
    
    Acto.objects.bulk_create(actos_a_crear)
    print(f"Éxito: {n} actos creados.")