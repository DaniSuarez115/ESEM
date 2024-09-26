from django.urls import path, include
from . import views

urlpatterns = [
     path('medallas/',views.medallas, name="medallas"),
     path('titulos/',views.titulos, name="titulos")
     
]