from django import forms
from .models import Desocupado

class DesocupadoForm(forms.ModelForm):

    class Meta:
        model = Desocupado
        fields = ('NOMBRE','APELLIDO','DNI', 'FECHA DE NACIMIENTO', 'EXPERIENCIA LABORAL', 'FORMACION', 'HABILIDADES',)