from rest_framework import serializers

from core.models import Pavio


class PavioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pavio
        fields = '__all__'
