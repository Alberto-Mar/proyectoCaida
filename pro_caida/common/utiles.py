from users.models import Hermano

def get_users_all():
    usuarios = Hermano.objects.all()
    return usuarios