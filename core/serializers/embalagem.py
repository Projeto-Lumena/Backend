from rest_framework import serializers
from core.models import Embalagem


class EmbalagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embalagem
        fields = '__all__'