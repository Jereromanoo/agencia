from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm

class Desocupado(models.Model):

        nombre = models.CharField(max_length=20)
        apellido = models.CharField(max_length=20)
        dni = models.CharField(max_length=8)
        fechaDeNacimiento = models.CharField(max_length=20)
        experienciaLaboral = models.TextField(max_length=200)
        formacion = models.TextField(max_length=200)
        habilidades = models.TextField(max_length=200)

class DesocupadoForm(ModelForm):
    
    class Meta:
        model = Desocupado
        fields = "__all__" 
def __unicode__(self):
        return self.dni

