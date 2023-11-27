from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect
from .forms import CuestionarioForm, RegistroForm
from .models import RespuestaCuestionario, Categoria  # Actualizamos la importación

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
            form.save()
            return redirect('formulario.html')  # Cambia 'login' con la URL correcta para redirigir al inicio de sesión
    else:
        form = RegistroForm()

    return render(request, 'signup.html', {'form': form})
def apariencia_fisica(request):
    plantilla = get_template('template_apariencia_fisica.html')
    return HttpResponse(plantilla.render())
def ciberacoso(request):
    plantilla = get_template('template_ciberacoso.hmtl')
    return HttpResponse(plantilla.render())

def discapacidad(request):
    plantilla = get_template('template_discapacidad')
    return HttpResponse(plantilla.render())

def orientacion_genero(request):
    plantilla = get_template(' template_genero_orientacion')
    return HttpResponse(plantilla.render())


def clasificacion(request):
    return render(request, 'clasificacion.html')

def mostrar_cuestionario(request):
    if request.method == 'POST':
        form = CuestionarioForm(request.POST)
        if form.is_valid():
            cuestionario = form.save(commit=False)
            cuestionario.calcular_puntaje_y_categoria()
            cuestionario.save()

            # Obtener la categoría del cuestionario
            categoria = cuestionario.categoria

            # Obtener la URL del template correspondiente
            template_url = categoria.obtener_template_categoria()

            # Renderizar directamente la plantilla en lugar de redirigir
            return render(request, template_url, {'cuestionario': cuestionario})
    else:
        form = CuestionarioForm()

    return render(request, 'cuestionario.html', {'form': form})

def vista_resultado(request, pk):
    cuestionario = RespuestaCuestionario.objects.get(pk=pk)  # Actualizamos la referencia al modelo
    return render(request, "resultado.html", {"cuestionario": cuestionario})