from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Medallas
from .models import Titulos

# Create your views here.
def medallas(request):
    medals = Medallas.objects.all()
    paginator = Paginator(medals, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'reconocimientos/html/medallas/MedallasLista.html', {'page_obj':page_obj})

def titulos(request):
    titles = Titulos.objects.all()
    paginator = Paginator(titles, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'reconocimientos/html/titulos/TitulosLista.html', {'page_obj':page_obj})

def reconocimientos(request):
    return render(request, 'reconocimientos/html/reconocimientos.html')