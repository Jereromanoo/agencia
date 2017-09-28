from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm
from django.core.urlresolvers import reverse_lazy

class Perfiles(models.Model):
    usuario = models.OneToOneField(User)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=8)
    fechaDeNacimiento = models.DateField(max_length=20)
    experienciaLaboral = models.TextField(max_length=200)
    formacion = models.TextField(max_length=200)
    habilidades = models.TextField(max_length=200)
    trabajo = models.TextField(max_length=200, blank=True)

    def __unicode__(self):
        return self.usuario.username

class Trabajos(models.Model):
	cargo = models.CharField(max_length=20)
	descripcion = models.TextField(max_length=200)
	horario = models.CharField(max_length=20)
	profesion = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.cargo

class Empresa(models.Model):
	nombre = models.CharField(max_length=20)
	cuit = models.CharField(max_length=11)
	razonSocial = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=25)
	logo = models.ImageField(upload_to='static/images'
	rubro = models.CharField(max_length=20)
