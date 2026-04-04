from rest_framework.viewsets import ModelViewSet

from core.models import Recipiente
from core.serializers import RecipienteSerializer

class RecipienteViewSet(ModelViewSet):  
    queryset = Recipiente.objects.all()
    serializer_class = RecipienteSerializer