from django import forms
from .models import Cuestionario

class CuestionarioForm(forms.ModelForm):
    class Meta:
        model = Cuestionario
        fields = ['pregunta_1', 'pregunta_2', 'pregunta_3', 'pregunta_4', 'pregunta_5', 'pregunta_6', 'pregunta_7', 'pregunta_8', 'pregunta_9']
