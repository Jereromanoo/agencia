from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from .models import Desocupado
from .models import DesocupadoForm
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from agenciaP.forms import LoginForm
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def add_desocupado(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = DesocupadoForm(request.POST) # Bound form
        if form.is_valid():
            new_persona = form.save() # Guardar los datos en la base de datos

            return HttpResponseRedirect(reverse_lazy('desocupados:login'))
    else:
        form = DesocupadoForm() # Unbound form

    return render(request, 'agenciaP/registrar.html', {'form': form})



class DesocupadoList(ListView):
	model = Desocupado
	template_name = "agenciaP/desocupados_list.html"

