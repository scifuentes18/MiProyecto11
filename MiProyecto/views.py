# Request: Para realizar peticiones
# HttpRespones: Para enviar la respuesta usando HHTP

# Esto es una vista
from django.http import HttpResponse


def bienvenidaRojo(request): #Objeto de tipo request como primer argumento
    return HttpResponse("<p style= 'color: red;'>Bienvenido o bienvenida a nuestra pagina : )</p>")