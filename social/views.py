from django.shortcuts import render
from .models import Publicacion

def publicaciones(request):
    publicacion = Publicacion.objects.all()
    return render(request, 'social/html/publicaciones/publicacionesLista.html',{'publicaciones':publicacion})

def socialMenu(request):
    
    return render(request, 'social/html/socialMenu/socialMenu.html')