from django.urls import path, include
from . import views
from social import views as social_views
urlpatterns = [
     path('publicaciones/', include('social.urls')),
     path('socialMenu/',social_views.socialMenu, name="socialMenu"),


     
     path('',views.home, name="home"),
     path('login/',views.login, name="login"),
     path('configuraciones/',views.configuraciones, name="configuraciones"),
     path('usuarios/',views.usuarios, name="usuarios"),
     path('register/',views.userRegister, name="register"),
     path('recover/',views.userRecover, name="recover"),
]