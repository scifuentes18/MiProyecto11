from django.contrib import admin
from django.urls import include, path
from Aplicaciones.views import home, formulario, signup, clasificacion, mostrar_cuestionario, apariencia_fisica, ciberacoso, discapacidad, orientacion_genero

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', formulario, name='login'),
    path('signup/', signup, name='signup'),
    path('clasificacion/', clasificacion, name='clasificacion'),
    path('cuestionario/', mostrar_cuestionario, name='cuestionario'),
    path('template_apariencia_fisica/', apariencia_fisica, name='apariencia_fisica'),
    path('ciberacoso/', ciberacoso, name= 'ciberacoso'),
    path('discapacidad/', discapacidad, name= 'discapacidad'),
    path('orientacion_genero/', orientacion_genero, name ='orientacion_genero'),

    ]
