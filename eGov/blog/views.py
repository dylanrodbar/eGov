from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Comments, Posts
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
from django.core.urlresolvers import reverse



def newProject(request):
    return render(request, 'blog/newProyecto.html')

def newNoticia(request):
    return render(request, 'blog/newNoticia.html')

def Profile(request):
    return render(request, 'blog/profile.html')

template_name = 'blog/postProyectos.html'


def Noticias(request):
    noticias = Posts.objects.all()[:25]
    template = loader.get_template('blog/noticias.html')
    print(noticias)
    context = {
    	'noticias': noticias 
    }
    return HttpResponse(template.render(context, request))

def Proyectos(request):
    proyectos = Posts.objects.all()[:25]
    template = loader.get_template('blog/proyectos.html')
	
    context = {
    	'proyectos': proyectos 
    }
    return HttpResponse(template.render(context, request))



def NoticiasDetail(request, id):
    
    print(request)
    post = get_object_or_404(Posts, pk=id)
    cur = connection.cursor()
    cur.callproc('commentsPost', [id,])
    comentarios = cur.fetchall()
    cur.close 
    template = loader.get_template('blog/PostNoticias.html')
    print(comentarios)

    context = {
    'post': post,
    'comentarios': comentarios,
    'id': id
    }
    return HttpResponse(template.render(context, request))

def ProyectosDetail(request, id):
    post = get_object_or_404(Posts, pk=id)
    template = loader.get_template('blog/PostProyectos.html')
    context = {
    'post': post
    }
    return HttpResponse(template.render(context, request))


def insertComment(request, id):

    template = loader.get_template('blog/PostNoticias.html')
    comment = request.POST.get('comment')
    cur = connection.cursor()
    cur.callproc('EGSP_InsertComment', [comment, 1, 1, '2017-03-03'])
    cur.close
    context = {}
    #return redirect('postNoticias', id=idk)
    return HttpResponseRedirect(reverse('blog:postNoticias', args=[id])) 
    