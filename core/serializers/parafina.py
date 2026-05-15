from rest_framework.serializers import ModelSerializer

from core.models import Parafina


class ParafinaSerializer(ModelSerializer):
    class Meta:
        model = Parafina
        fields = '__all__'
