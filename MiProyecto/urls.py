# urls.py
from django.contrib import admin
from django.urls import include, path
<<<<<<< HEAD
from Aplicaciones.views import home, formulario, signup, clasificacion, mostrar_cuestionario, apariencia_fisica, ciberacoso, discapacidad, orientacion_genero
=======
from Aplicaciones.views import home, pagina1, formulario, signup, mostrar_cuestionario, vista_resultado
>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
<<<<<<< HEAD
    path('login/', formulario, name='login'),
    path('signup/', signup, name='signup'),
    path('clasificacion/', clasificacion, name='clasificacion'),
    path('cuestionario/', mostrar_cuestionario, name='cuestionario'),
    path('template_apariencia_fisica/', apariencia_fisica, name='apariencia_fisica'),
    path('ciberacoso/', ciberacoso, name= 'ciberacoso'),
    path('discapacidad/', discapacidad, name= 'discapacidad'),
    path('orientacion_genero/', orientacion_genero, name ='orientacion_genero'),
=======
    path('pagina/', pagina1, name='pagina1'),
    path('login/', formulario, name='login'),
    path('signup/', signup, name='signup'),
    path('cuestionario/', mostrar_cuestionario, name='cuestionario'),
    path('mostrar_cuestionario/', mostrar_cuestionario, name='mostrar_cuestionario'),
    path('vista_resultado/<int:pk>/', vista_resultado, name='vista_resultado'),
    # Agrega más rutas para otras vistas según sea necesario
]
>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4

    ]
