from django.shortcuts import render
from blog.models import Comment, Post
from django.views import generic

class NoticiasDetail(generic.DetailView):
    model=Post
    context_object_name = 'post'
    template_name = 'blog/postNoticias.html'


class ProyectosDetail(generic.DetailView):
    model=Post
    context_object_name = 'post'
    template_name = 'blog/postProyectos.html'
