<<<<<<< HEAD
=======
# views.py
>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect
from .forms import CuestionarioForm, RegistroForm
<<<<<<< HEAD
from .models import RespuestaCuestionario, Categoria  # Actualizamos la importación
=======
from .models import RespuestaCuestionario, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4

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
<<<<<<< HEAD
            form.save()
            return redirect('formulario.html')  # Cambia 'login' con la URL correcta para redirigir al inicio de sesión
=======
            user = form.save()

            # Inicia sesión automáticamente después de registrar al usuario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

            # Redirige al usuario a la página del cuestionario
            return redirect('cuestionario')  # Ajusta esto según la URL de tu cuestionario
>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4
    else:
        form = RegistroForm()

    return render(request, 'signup.html', {'form': form})
<<<<<<< HEAD
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

=======

def clasificacion(request, pk):
    cuestionario = RespuestaCuestionario.objects.get(pk=pk)
    return render(request, 'clasificacion.html', {'cuestionario': cuestionario})

@login_required
>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4
def mostrar_cuestionario(request):
    if request.method == 'POST':
        form = CuestionarioForm(request.POST)
        if form.is_valid():
            cuestionario = form.save(commit=False)
<<<<<<< HEAD
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
=======
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
>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4
