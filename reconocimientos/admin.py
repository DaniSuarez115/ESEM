from django.contrib import admin
from .models import Medallas
from .models import Titulos


class MedallasAdmin(admin.ModelAdmin):
     readonly_fields =('created','updated')

admin.site.register(Medallas,MedallasAdmin)

class TitulosAdmin(admin.ModelAdmin):
     readonly_fields =('created','updated')

admin.site.register(Titulos,TitulosAdmin)