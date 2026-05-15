from rest_framework.serializers import ModelSerializer

from core.models import Recipiente


class RecipienteSerializer(ModelSerializer):
    class Meta:
        model = Recipiente
        fields = '__all__'
