from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login
urlpatterns = [
        url(r'^desocupados', views.DesocupadoList.as_view(), name='desocupados'),
        url(r'^registrar/$', views.add_desocupado, name='dadd'),
    	url(r'^(?!.)', login, {'template_name': 'agenciaP/login.html'}, name='login'),
    ]