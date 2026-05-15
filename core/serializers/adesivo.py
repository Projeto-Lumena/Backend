from rest_framework.serializers import ModelSerializer

from core.models import Adesivo


class AdesivoSerializer(ModelSerializer):
    class Meta:
        model = Adesivo
        fields = '__all__'
