from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [ 
                url(r'^noticias/$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="blog/noticias.html")),

                url(r'^proyectos/$', ListView.as_view(
                                   queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="blog/proyectos.html")),

                url(r'^noticias/(?P<pk>\d+)$',views.NoticiasDetail.as_view(), name='postNoticias'),


                url(r'^proyectos/(?P<pk>\d+)$', views.ProyectosDetail.as_view(), name='postProyectos'),
            ]
