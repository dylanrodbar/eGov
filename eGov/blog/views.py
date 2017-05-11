from django.shortcuts import render, get_object_or_404
from blog.models import Comment, Post
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from django.db import connection

def newProject(request):
    return render(request, 'blog/newProyecto.html')

def newNoticia(request):
    return render(request, 'blog/newNoticia.html')

def Profile(request):
    return render(request, 'blog/profile.html')

#class NoticiasDetail(generic.DetailView):
#    model=Post
#    context_object_name = 'post'
#    template_name = 'blog/postNoticias.html'


#class ProyectosDetail(generic.DetailView):
#    model=Post
#    context_object_name = 'post'
#    template_name = 'blog/postProyectos.html'


def Noticias(request):
	noticias = Post.objects.all()[:25]
	template = loader.get_template('blog/noticias.html')
	print(noticias)
	context = {
		'noticias': noticias 
	}
	return HttpResponse(template.render(context, request))

def Proyectos(request):
	proyectos = Post.objects.all()[:25]
	template = loader.get_template('blog/proyectos.html')
	
	context = {
		'proyectos': proyectos 
	}
	return HttpResponse(template.render(context, request))



def NoticiasDetail(request, id):
	post = get_object_or_404(Post, pk=id)
	cur = connection.cursor()
	cur.callproc('commentsPost', [id,])
	comentarios = cur.fetchall()
	cur.close 
	template = loader.get_template('blog/PostNoticias.html')
	print(comentarios)

	context = {
        'post': post,
        'comentarios': comentarios
	}
	return HttpResponse(template.render(context, request))

def ProyectosDetail(request, id):
	post = get_object_or_404(Post, pk=id)
	template = loader.get_template('blog/PostProyectos.html')
	context = {
        'post': post
	}
	return HttpResponse(template.render(context, request))


