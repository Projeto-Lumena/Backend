from rest_framework import serializers

from core.models import Parafina


class ParafinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parafina
        fields = '__all__'
