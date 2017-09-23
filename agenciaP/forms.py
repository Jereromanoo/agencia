from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class JobForm(UserCreationForm):
	cargo = forms.CharField()
	descripcion = forms.CharField()
	horario = forms.CharField()
	profesion = forms.CharField()

