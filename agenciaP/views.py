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
from .models import Perfiles, Trabajos, Empresa  



class registrar(FormView):
    template_name = "agenciaP/registrar.html"
    form_class = UserForm
    success_url = reverse_lazy('login') 

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

class registrarempresa(FormView):
    template_name = "agenciaP/regEmpresa.html"
    form_class = UserForm
    success_url = reverse_lazy('login') 

    def form_valid(self, form):
        user = form.save()
        perfil = Empresa()
        perfil.empresa= user
        perfil.nombre = form.cleaned_data['nombre']
        perfil.cuit = form.cleaned_data['cuit']
        perfil.razonSocial = form.cleaned_data['razonSocial']
        perfil.descripcion = form.cleaned_data['descripcion']
        perfil.rubro = form.cleaned_data['rubro']
        """perfil.logo = form.ImageField['logo']  """
        perfil.save()
        return super(registrarempresa , self).form_valid(form)


class DesocupadoList(ListView):
	model = Perfiles
	template_name = "agenciaP/desocupados_list.html"


def trabajos_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('trabajos', request=request)
    else:
        form =JobForm()
    return render(request, 'agenciaP/registrartrabajo.html', {'form':form})

class TrabajoList(ListView):
	model = Trabajos
	template_name = "agenciaP/trabajos_list.html"



#def eliminarDesocupado(request, object_id):
#    object = get_object_or_404(Perfiles, pk=object_id)
#    object.delete()

