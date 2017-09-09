from django.db import models
from django.utils import timezone

class Desocupado(models.Model):
        nombre = models.CharField(max_length=20)
        apellido = models.CharField(max_length=20)
        dni = models.CharField(max_length=8)
        fechaDeNacimiento = models.CharField(max_length=20)
        experienciaLaboral = models.TextField(max_length=200)
        formacion = models.TextField(max_length=200)
        habilidades = models.TextField(max_length=200)


def publish(self):
            self.published_date = timezone.now()
            self.save()

def __str__(self):
     return self.title

