from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trabajos

class UserForm(UserCreationForm):
	nombre = forms.CharField()
	apellido = forms.CharField()
	dni = forms.CharField()
	fechaDeNacimiento = forms.CharField()
	experienciaLaboral = forms.CharField()
	formacion = forms.CharField()
	habilidades = forms.CharField()
	trabajo = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class JobForm(forms.ModelForm):
	
	class Meta:
		model = Trabajos

		fields = [
			'cargo',
			'descripcion',
			'horario',
			'profesion',
		]
		labels = {
			'cargo': 'Cargo',
			'descripcion' : 'Descripcion',
			'horario' : 'Horario',
			'profesion' : 'Profesion',
		}
		widgets = {
			'cargo': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'horario': forms.TextInput(attrs={'class':'form-control'}),
			'profesion': forms.TextInput(attrs={'class':'form-control'}),
		}

