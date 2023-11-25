# urls.py
from django.contrib import admin
from django.urls import include, path
from Aplicaciones.views import home, pagina1, formulario, signup, mostrar_cuestionario, vista_resultado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('pagina/', pagina1, name='pagina1'),
    path('login/', formulario, name='login'),
    path('signup/', signup, name='signup'),
    path('cuestionario/', mostrar_cuestionario, name='cuestionario'),
    path('mostrar_cuestionario/', mostrar_cuestionario, name='mostrar_cuestionario'),
    path('vista_resultado/<int:pk>/', vista_resultado, name='vista_resultado'),
    # Agrega más rutas para otras vistas según sea necesario
]

