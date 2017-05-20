from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contacto/$', views.contact, name='contact'),
    url(r'^contacto/enviarCorreo/$', views.enviarCorreo, name='enviarCorreo'),
    ]
