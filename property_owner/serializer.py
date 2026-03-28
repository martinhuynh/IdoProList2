# In your app's serializers.py
from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'description', 'street', 'city', 'state', 'zip_code', 'created_at', 'last_updated']
