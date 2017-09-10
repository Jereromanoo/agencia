from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from agenciaP.forms import RegistroForm
# Create your views here.
class RegistroUsuario(CreateView):
	model = User
	template_name = "agenciaP/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('oferta:oferta_lista')


def desocupados_list(request):
        return render(request, 'agenciaP/desocupados_list.html', {})