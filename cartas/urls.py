from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cartas, name='lista_cartas'),
    path('<int:carta_id>/', views.detalle_carta, name='detalle_carta'),
    path('nueva/', views.nueva_carta, name='nueva_carta'),
]