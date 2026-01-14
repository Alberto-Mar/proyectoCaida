from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Hermano, RolReservado

# Register your models here.

class HermanoAdmin(admin.ModelAdmin):
    model = Hermano
    list_display = ['email', 'username', 'cargo_junta', 'is_active']
    ordering = ['email']
    
    def save_model(self, request, obj, form, change):
        if not change or 'password' in form.changed_data:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)
        
admin.site.register(Hermano, HermanoAdmin)
admin.site.register(RolReservado)