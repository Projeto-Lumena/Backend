from rest_framework.viewsets import ModelViewSet
from core.models import Aroma
from core.serializers import AromaSerializer

class AromaViewSet(ModelViewSet):  
    queryset = Aroma.objects.all()
    serializer_class = AromaSerializer