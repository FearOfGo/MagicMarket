from django.db import models
from django.contrib.auth.models import User
from .choices import ESTADOS_CARTAS, RAREZAS, IDIOMAS, JUEGOS 


class Carpeta(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carpetas')

class Carta(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='cartas/', null=True, blank=True)
    juego = models.CharField(max_length=10, choices=JUEGOS)
    edicion = models.CharField(max_length=100)
    rareza = models.CharField(max_length=5, choices=RAREZAS)
    estado = models.CharField(max_length=2, choices=ESTADOS_CARTAS)
    idioma = models.CharField(max_length=2, choices=IDIOMAS)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
    visitas = models.PositiveIntegerField(default=0)



    en_venta = models.BooleanField(default=True)
    vendida = models.BooleanField(default=False)
    fecha_agregada = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartas')

    def __str__(self):
        return f"{self.nombre} ({self.edicion})"

    class Meta:
        ordering = ['-fecha_agregada']