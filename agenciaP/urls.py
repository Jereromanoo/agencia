from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login, logout_then_login
from .views import registrar
from django.contrib.auth.decorators import login_required


urlpatterns = [
        url(r'^desocupados', login_required(views.DesocupadoList.as_view()), name='desocupados'),
        url(r'^registrar/$', registrar.as_view(), name='registrarse'),
    	url(r'^accounts/login/', login, {'template_name': 'agenciaP/login.html'}, name='login'),
    	url(r'^logout/', logout_then_login, name='logout'),
    ]