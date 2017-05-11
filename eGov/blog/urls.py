from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from blog.models import Posts

urlpatterns = [ 
                url(r'^noticias/$', views.Noticias, name='noticias'),

                url(r'^insertPost/$', views.insertPost, name='insertPost'),

                url(r'^proyectos/$', views.Proyectos, name='proyectos'),

                url(r'^noticias/(?P<id>[0-9]+)$',views.NoticiasDetail, name='postNoticias'),


                url(r'^proyectos/(?P<id>[0-9]+)/$', views.ProyectosDetail, name='postProyectos'),
                
                url(r'^proyectos/new/$', views.newProject, name='newP'),

                url(r'^noticias/new/$', views.newNoticia, name='newN'),


                url(r'^perfil/$', views.Profile, name='Pefil'),

                url(r'^comentario/(?P<id>[0-9]+)$',views.insertComment, name='insertComment'),

                
            ]
