from rest_framework.viewsets import ModelViewSet
from core.models import Cardapio
from core.serializers import CardapioSerializer

class CardapioViewSet(ModelViewSet):
    queryset = Cardapio.objects.all().order_by('id')
    serializer_class = CardapioSerializer
