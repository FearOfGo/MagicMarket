from django.db import models
from django.contrib.auth.models import User


class Carpeta(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carpetas')

class Carta(models.Model):
    ESTADO_CHOICES = [
        ('NM', 'Como Nueva'),
        ('LP', 'Poco Jugada'),
        ('MP', 'Medianamente jugada'),
        ('HP', 'Muy jugada'),
        ('DMG', 'Dañada'),
    ]


    nombre = models.CharField(max_length=100)
    edicion = models.CharField(max_length=100, blank=True)
    tipo = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='cartas/', blank=True, null=True)
    estado = models.CharField(max_length=4, choices=ESTADO_CHOICES, default='NM' )
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartas')
    carpeta = models.ForeignKey('Carpeta', on_delete=models.CASCADE, related_name='cartas', null=True, blank=True)
    visitas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.edicion})"