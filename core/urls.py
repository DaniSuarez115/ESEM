from django.urls import path, include
from . import views

urlpatterns = [
     path('',views.home, name="home"),
     path('login/',views.login, name="login"),
     path('configuraciones/',views.configuraciones, name="configuraciones"),
     path('usuarios/',views.usuarios, name="usuarios")
     
]