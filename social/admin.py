from django.contrib import admin
from .models import Publicacion
# Register your models here.
class PublicacionAdmin(admin.ModelAdmin):
     readonly_fields =('created','updated')
     list_display = ('titulo','descripcion','fecha','user')
     ordering = ('titulo','descripcion','fecha','user')
     search_fields =  ('titulo','descripcion','fecha','user')
     date_hierarchy =('fecha')
     list_filter  = ('titulo','descripcion','fecha','user')
admin.site.register(Publicacion,PublicacionAdmin)
