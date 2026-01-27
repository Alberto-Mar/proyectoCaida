from rest_framework import serializers
from users.models import Hermano

class HermanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hermano
        fields = '__all__'