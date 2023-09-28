from django.db import models

class Usuario(models.Model):
    correo_electronico = models.EmailField(unique=True)
    nombre = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=128)
    esta_activo = models.BooleanField(default=True)
    es_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.correo_electronico


