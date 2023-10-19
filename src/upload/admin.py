from .models import Person, AuditLog
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'is_superuser') 
    search_fields = ('username', 'first_name', 'last_name', 'phone_number', 'email') 
    ordering = ('username',) 
    exclude = ('last_login', 'date_joined', 'groups', 'user_permissions', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)

class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('username', 'action', 'timestamp', 'before', 'after')  # Customize the displayed fields as needed

# Register the AuditLog model with the custom admin class
admin.site.register(AuditLog, AuditLogAdmin)

admin.site.register(Person)