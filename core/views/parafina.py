from rest_framework.viewsets import ModelViewSet
from core.models import Parafina
from core.serializers import ParafinaSerializer

class ParafinaViewSet(ModelViewSet):    
    queryset = Parafina.objects.all()
    serializer_class = ParafinaSerializer