from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^login/redirectNoticias$', views.redirectNoticias, name='redirectNoticias'),
    url(r'^login/redirectProyectos$', views.redirectProyectos, name='redirectProyectos'),
    url(r'^login/redirectPerfil$', views.redirectPerfil, name='redirectPerfil'),
    url(r'^salir$', views.salir, name='salir'),
    ]
