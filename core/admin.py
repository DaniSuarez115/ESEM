from django.contrib import admin
from .models import Usuarios
# Register your models here.
class UsuariosAdmin(admin.ModelAdmin):
     readonly_fields =('created','updated')

admin.site.register(Usuarios,UsuariosAdmin)