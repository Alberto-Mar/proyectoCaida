from rest_framework import mixins, viewsets, filters
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
    
class HermanoListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = HermanoSerializer
    pagination_class = HermanoPagination
    filter_backends = (filters.OrderingFilter, )
    ordering = 'numero_hermano' # orden default (no sale en la url)
    ordering_fields = ['numero_hermano', 'email'] # campos permitidos para ordenar via url
    
    def get_queryset(self): # filtrar por numero_hermano desde la url
        num_hermano_from = self.request.query_params.get('num_hermano_from')
        if num_hermano_from:
            return Hermano.objects.filter(numero_hermano__gte=num_hermano_from)
        return Hermano.objects.all()
    