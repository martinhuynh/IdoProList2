# In your app's serializers.py
from rest_framework import serializers
from .models import Property, WorkOrder

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'description', 'street', 'city', 'state', 'zip_code', 'created_at', 'last_updated']

class WorkOrderInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ['description', 'property_id', 'user_id']

class WorkOrderOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ['id', 'description', 'property_id', 'status', 'user_id']