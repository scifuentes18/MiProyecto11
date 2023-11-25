# views.py
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect
from .forms import CuestionarioForm, RegistroForm
from .models import RespuestaCuestionario, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def home(request):
    plantilla = get_template('index.html')
    return HttpResponse(plantilla.render())

def pagina1(request):
    return HttpResponse("Nueva ruta")

def formulario(request):
    plantilla = get_template('formulario.html')
    return HttpResponse(plantilla.render())

def signup(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Inicia sesión automáticamente después de registrar al usuario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

            # Redirige al usuario a la página del cuestionario
            return redirect('cuestionario')  # Ajusta esto según la URL de tu cuestionario
    else:
        form = RegistroForm()

    return render(request, 'signup.html', {'form': form})

def clasificacion(request, pk):
    cuestionario = RespuestaCuestionario.objects.get(pk=pk)
    return render(request, 'clasificacion.html', {'cuestionario': cuestionario})

@login_required
def mostrar_cuestionario(request):
    if request.method == 'POST':
        form = CuestionarioForm(request.POST)
        if form.is_valid():
            cuestionario = form.save(commit=False)
            cuestionario.usuario = request.user
            cuestionario.save()

            # Calcular la categoría y obtener la URL del template
            categoria_nombre = cuestionario.categoria.calcular_puntaje_y_categoria(
                cuestionario.pregunta_1, cuestionario.pregunta_2, cuestionario.pregunta_3
            )
            template_url = Categoria.objects.get(nombre=categoria_nombre).obtener_template_categoria()

            # Redirigir a la vista correspondiente
            return redirect('vista_resultado', pk=cuestionario.pk)
    else:
        form = CuestionarioForm()
        del form.fields['categoria']

    return render(request, 'cuestionario.html', {'form': form})
def vista_resultado(request, pk):
    cuestionario = RespuestaCuestionario.objects.get(pk=pk)
    template_categoria = cuestionario.categoria.obtener_template_categoria()
    return render(request, template_categoria, {"cuestionario": cuestionario})
