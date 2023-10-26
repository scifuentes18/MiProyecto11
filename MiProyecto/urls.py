from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pagina/', views.pagina1, name='pagina1'),
    path('login/', views.formulario, name='login'),
    path('signup/', views.signup, name='signup'),
    path('cuestionario/', views.mostrar_cuestionario, name='cuestionario')
]

    
   

