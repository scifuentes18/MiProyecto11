from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, RespuestaCuestionario

class RegistroForm(UserCreationForm):
    telefono = forms.CharField(max_length=15, required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'telefono', 'password1', 'password2']


class CuestionarioForm(forms.ModelForm):
    class Meta:
        model = RespuestaCuestionario
        exclude = ['usuario', 'puntaje_total', 'categoria']
