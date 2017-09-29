from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login, logout_then_login
from .views import registrar, registrarempresa, trabajos_view, editar
from django.contrib.auth.decorators import login_required


urlpatterns = [
        url(r'^desocupados', login_required(views.DesocupadoList.as_view()), name='desocupados'),
        url(r'^trabajos', login_required(views.TrabajoList.as_view()), name='trabajos'),
        url(r'^registrar/$', registrar.as_view(), name='registrarse'),
        url(r'^registrartrabajo/$', trabajos_view, name='registrartrabajo'),
        url(r'^$', login, {'template_name': 'agenciaP/login.html'}, name='home'),

        url(r'^editar/(?P<user>\d+)/$', editar, name='editar'),
    	
        url(r'^accounts/login/', login, {'template_name': 'agenciaP/login.html'}, name='login'),
    	url(r'^logout/', logout_then_login, name='logout'),
		url(r'^registrarempresa/$', registrarempresa.as_view(), name='registrarempresa'),

    	url(r'^accounts/login/', login, {'template_name': 'agenciaP/login.html'}, name='login'),
    	url(r'^logout/', logout_then_login, name='logout'),
        url(r'^redireccion/$', login, {'template_name': 'agenciaP/redireccion.html'}, name='redireccion'),	

    ]
