from django.contrib import admin
from cartas import views as cartas_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from cartas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cartas_views.home, name='home'),
    path('cartas/', include('cartas.urls')),
    path('nueva/', views.nueva_carta, name='publicar_carta'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
