from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from agenciaP.forms import LoginForm, UserForm, JobForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from .models import Perfiles, Trabajos  



class registrar(FormView):
    template_name = "agenciaP/registrar.html"
    form_class = UserForm
    success_form = reverse_lazy('login') 

    def form_valid(self, form):
        user = form.save()
        perfil = Perfiles()
        perfil.usuario = user
        perfil.nombre = form.cleaned_data['nombre']
        perfil.apellido = form.cleaned_data['apellido']
        perfil.dni = form.cleaned_data['dni']
        perfil.fechaDeNacimiento = form.cleaned_data['fechaDeNacimiento']
        perfil.experienciaLaboral = form.cleaned_data['experienciaLaboral']
        perfil.formacion = form.cleaned_data['formacion']
        perfil.habilidades = form.cleaned_data['habilidades']
        perfil.trabajo = form.cleaned_data['trabajo']
        perfil.save()
        return super(registrar , self).form_valid(form)


class DesocupadoList(ListView):
	model = Perfiles
	template_name = "agenciaP/desocupados_list.html"


def trabajos_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('desocupados')
    else:
        form =JobForm()
    return render(request, 'agenciaP/registrartrabajo.html', {'form':form})






