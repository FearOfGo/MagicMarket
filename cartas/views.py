from django.shortcuts import render, get_object_or_404, redirect
from .models import Carta
from django.contrib.auth.models import User
from .forms import CartaForm

def home(request):
    cartas_populares = Carta.objects.order_by('-visitas')[:10]
    contexto = {
        'cartas_populares': cartas_populares,
        'noticias':[],
    }
    return render(request, 'cartas/home.html', contexto)


def lista_cartas(request):
    cartas = Carta.objects.all().order_by('-fecha_publicacion')
    return render(request, 'cartas/lista_cartas.html', {'cartas' : cartas})

def detalle_carta(request, carta_id):
    carta = get_object_or_404(Carta, pk=carta_id)
    return render(request, 'cartas/detalle_carta.html', {'carta' : carta})


def nueva_carta(request):
    if request.method == 'POST':
        form = CartaForm(request.POST, request.FILES, usuario=request.user)
        if form.is_valid():
            nueva = form.save(commit=False)
            nueva.usuario = request.user
            nueva.save()
            return redirect('detalle_carta', carta_id=nueva.id)
    else:
        form = CartaForm(usuario=request.user)
    return render(request, 'cartas/nueva_carta.html', {'form': form})

def perfil_usuario(request, username):
    usuario = get_object_or_404(User, username=username)
    cartas = Carta.objects.filter(usuario=usuario)

    return render(request, 'cartas/perfil.html', {
        'usuario_perfil' : usuario,
        'cartas' : cartas,
    })