from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, RespuestaCuestionario

class RegistroForm(UserCreationForm):
    telefono = forms.CharField(max_length=15, required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'telefono', 'password1', 'password2']

<<<<<<< HEAD

class CuestionarioForm(forms.ModelForm):
    class Meta:
        model = RespuestaCuestionario
        exclude = ['usuario', 'puntaje_total', 'categoria']
=======
class CuestionarioForm(forms.ModelForm):
    class Meta:
        model = RespuestaCuestionario
        fields = '__all__'
        widgets = {'categoria': forms.HiddenInput(), 'usuario': forms.HiddenInput()}
>>>>>>> 0771c18659a3602f5df4adcb586b93171e4256b4
