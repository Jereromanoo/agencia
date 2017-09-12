from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login
from .views import registrar
urlpatterns = [
        url(r'^desocupados', views.DesocupadoList.as_view(), name='desocupados'),
        url(r'^registrar/$', registrar.as_view(), name='registrarse'),
    	url(r'^(?!.)', login, {'template_name': 'agenciaP/login.html'}, name='login'),

    ]