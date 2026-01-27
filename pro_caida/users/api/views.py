from rest_framework import mixins, viewsets
from users.models import Hermano
from .serializers import HermanoSerializer
from .pagination import HermanoPagination

class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = HermanoSerializer
    pagination_class = HermanoPagination
    
    def get_queryset(self):
        return Hermano.objects.all()
    
class HermanoCrudViewSet(viewsets.ModelViewSet):
    queryset = Hermano.objects.all()
    serializer_class = HermanoSerializer
    
    
    
    