from django.contrib import admin

from .models import Property

class CustomProperty(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'state', 'zip_code']

# Register your models here.
admin.site.register(Property, CustomProperty)