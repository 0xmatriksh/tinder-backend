from rest_framework import serializers
from .models import People

class PeopleSerializer(serializers.ModelSerializer):
    ext_link = serializers.ReadOnlyField()
    class Meta:
        fields = '__all__'
        model = People