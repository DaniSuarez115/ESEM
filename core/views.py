from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return render(request, 'core/html/login.html')

def home(request):
    return render(request, 'core/html/home.html')