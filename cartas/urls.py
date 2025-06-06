from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import perfil_usuario

urlpatterns = [

    #Login-Logout
    path('login/', auth_views.LoginView.as_view(template_name='cartas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),


    path('', views.lista_cartas, name='lista_cartas'),
    path('<int:carta_id>/', views.detalle_carta, name='detalle_carta'),
    path('nueva/', views.nueva_carta, name='nueva_carta'),

    #Perfil Usuario 
    path('perfil/<str:username>/', perfil_usuario, name='perfil_usuario'),

    path('buscar', views.buscar_cartas, name='buscar_cartas'),
]