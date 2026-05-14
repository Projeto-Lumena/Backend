from rest_framework.serializers import ModelSerializer

from core.models import Embalagem


class EmbalagemSerializer(ModelSerializer):
    class Meta:
        model = Embalagem
        fields = '__all__'
