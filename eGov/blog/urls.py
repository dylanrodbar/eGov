from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from blog.models import Posts

urlpatterns = [ 
                url(r'^noticias/$', views.Noticias, name='noticias'),

                url(r'^insertPost/$', views.insertPost, name='insertPost'),

                url(r'^insertProject/$', views.insertProject, name='insertProject'),

                url(r'^updateUser/$', views.updateUser, name='updateUser'),

                url(r'^proyectos/$', views.Proyectos, name='proyectos'),

                url(r'^noticias/(?P<id>[0-9]+)$',views.NoticiasDetail, name='postNoticias'),

            

                url(r'^noticias/aceptarNoticia/(?P<id>[0-9]+)$',views.aceptarNoticia, name='aceptarNoticia'),

                url(r'^noticias/rechazarNoticia/(?P<id>[0-9]+)$',views.rechazarNoticia, name='rechazarNoticia'),

                url(r'^proyectos/addYes/(?P<id>[0-9]+)/$', views.ProyectoAddYes, name='ProyectoAddYes'),

                url(r'^proyectos/addNo/(?P<id>[0-9]+)/$', views.ProyectoAddNo, name='ProyectoAddNo'),

                url(r'^proyectos/addUnknown/(?P<id>[0-9]+)/$', views.ProyectoAddUnknown, name='ProyectoAddUnknown'),

                url(r'^noticias/deletePost/(?P<id>[0-9]+)$',views.deletePost, name='deletePost'),

                url(r'^proyectos/(?P<id>[0-9]+)/$', views.ProyectosDetail, name='postProyectos'),
                
                url(r'^proyectos/new/$', views.newProject, name='newProject'),

                url(r'^noticias/new/$', views.newNoticia, name='newNoticia'),

                url(r'^noticias/editar/(?P<id>[0-9]+)$', views.editarNoticia, name='editarNoticia'),

                url(r'^noticias/editarEsp/(?P<id>[0-9]+)$', views.editarNoticiaEsp, name='editarNoticiaEsp'),

                url(r'^perfil/$', views.Profile, name='Perfil'),

                url(r'^comentario/(?P<id>[0-9]+)$',views.insertComment, name='insertComment'),
				
				url(r'^comentarioProyecto/(?P<id>[0-9]+)$',views.insertCommentProject, name='insertCommentProject'),


                
            ]
