from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id',) + UserAdmin.list_display
    # fieldsets = UserAdmin.fieldsets + UserAdmin.fieldsets['Personal info']['fields'].append('phone_number',)

# Register your models here.
admin.site.register(User, CustomUserAdmin)