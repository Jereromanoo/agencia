from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^desocupados', views.DesocupadoList.as_view(), name="desocupados"),
        url(r'^registrar', views.add_desocupado, name="dadd"),
    ]