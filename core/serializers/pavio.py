from rest_framework.serializers import ModelSerializer

from core.models import Pavio


class PavioSerializer(ModelSerializer):
    class Meta:
        model = Pavio
        fields = '__all__'
