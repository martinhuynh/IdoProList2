from django.contrib import admin

from .models import Property, WorkOrder

class CustomProperty(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'state', 'zip_code']

class CustomWorkOrder(admin.ModelAdmin):
    list_display = ['id', 'property_id', 'description', 'status', 'user_id']

# Register your models here.
admin.site.register(Property, CustomProperty)
admin.site.register(WorkOrder, CustomWorkOrder)