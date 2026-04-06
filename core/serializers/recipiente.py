from rest_framework import serializers
from core.models import Recipiente

class RecipienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipiente
        fields = '__all__'