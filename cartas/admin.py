from django.contrib import admin
from .models import Carta

class CartaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edicion', 'precio')
    search_fields = ('nombre', 'edicion')

