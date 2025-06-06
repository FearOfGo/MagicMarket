import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import User  # Importa User
from cartas.models import Carta

class Command(BaseCommand):
    help = "Carga cartas desde un archivo JSON"

    def handle(self, *args, **kwargs):
        usuario = User.objects.first()  # Usuario para asignar a las cartas

        if not usuario:
            self.stdout.write(self.style.ERROR("No hay usuarios disponibles para asignar las cartas"))
            return

        fixture_path = os.path.join(settings.BASE_DIR, 'cartas', 'fixtures', 'cartas_ejemplo.json')

        with open(fixture_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            carta = Carta(
                nombre=item.get('nombre', ''),
                juego=item.get('juego', ''),
                precio=item.get('precio', 0),
                usuario=usuario,  # Asignar usuario aquí
                # agrega más campos según tu modelo
            )
            carta.save()

        self.stdout.write(self.style.SUCCESS("Cartas cargadas correctamente"))
