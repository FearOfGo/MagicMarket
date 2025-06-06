from django import forms
from .models import Carta, Carpeta

class CartaForm(forms.ModelForm):
    class Meta:
        model = Carta
        fields = ['nombre',
                  'edicion',
                  'descripcion',
                  'estado',
                  'precio',
                  'imagen',]

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)