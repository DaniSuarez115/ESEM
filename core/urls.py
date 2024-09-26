from django.urls import path, include
from . import views
from reconocimientos import views as rec_views

urlpatterns = [
     path('reconocimientos/',include ('reconocimientos.urls')),
     
     path('',views.home, name="home"),
     path('login/',views.login, name="login"),
     path('configuraciones/',views.configuraciones, name="configuraciones"),
     path('usuarios/',views.usuarios, name="usuarios"),
     path('medallas/',rec_views.medallas, name="medallas"),
     path('titulos/',rec_views.titulos, name="titulos"),
     path('reconocimientos/',rec_views.reconocimientos, name="reconocimientos")
     
]