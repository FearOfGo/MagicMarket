from django import forms
from .models import Carta, Carpeta

class CartaForm(forms.ModelForm):
    class Meta:
        model = Carta
        fields = ['nombre',
                  'edicion',
                  'tipo',
                  'descripcion',
                  'estado',
                  'precio',
                  'imagen',
                  'carpeta']

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)
        if usuario:
           
            self.fields['carpeta'].queryset = Carpeta.objects.filter(usuario=usuario)
        else:
            self.fields['carpeta'].queryset = Carpeta.objects.none()