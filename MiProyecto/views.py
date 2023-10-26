# Request: Para realizar peticiones
# HttpRespones: Para enviar la respuesta usando HHTP

# Esto es una vista
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect
from .forms import CuestionarioForm
from .models import Cuestionario

def home(request):
    plantilla = get_template('index.html')
    return HttpResponse(plantilla.render())

def pagina1(request):
    return HttpResponse("Nueva ruta")

def formulario(request):
    plantilla = get_template('formulario.html')
    return HttpResponse(plantilla.render())

def signup(request):
    return render(request, 'signup.html')

def mostrar_cuestionario(request):
    if request.method == 'POST':
        form = CuestionarioForm(request.POST)
        if form.is_valid():
            cuestionario = form.save(commit=False)
            cuestionario.calcular_puntaje_y_categoria()
            cuestionario.save()
            return redirect('resultado_cuestionario')
    else:
        form = CuestionarioForm()

    return render(request, 'cuestionario.html', {'form': form})

def resultado_cuestionario(request):
    return render(request, 'resultado_cuestionario.html')



def vista_resultado(request, pk):
    cuestionario = Cuestionario.objects.get(pk=pk)
    return render(request, "resultado.html", {"cuestionario": cuestionario})
