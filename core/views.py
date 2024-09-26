from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from .models import Usuarios

# Create your views here.
def login(request):
    return render(request, 'core/html/login.html')

def userRegister(request):
    return render(request, 'core/html/usuarios/usuariosRegister.html')

def userRecover(request):
    return render(request, 'core/html/usuarios/usuariosRecover.html')

def usuarios(request):
    users = Usuarios.objects.all()
    paginator = Paginator(users, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/html/usuarios/usuariosLista.html', {'page_obj': page_obj})


def home(request):
    return render(request, 'core/html/home.html')

def configuraciones(request):
    return render(request, 'core/html/configuraciones.html')