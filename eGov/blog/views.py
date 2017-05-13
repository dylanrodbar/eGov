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
    user = int(request.session['Usuario'])
    
    cur = connection.cursor()
    cur.callproc('UserData', [user,])
    datos = cur.fetchall()
    print(datos)
    name = datos[0][0]
    lastname = datos[0][1]
    email = datos[0][2]
    path = datos[0][3]
    points = str(datos[0][4])+"%"
    
    print("holaaa")
    print(path)


    cur.nextset()
    cur.callproc('PostsXUser', [user,])
    posts = cur.fetchall()
    cur.close
    context = {
        'name': name,
        'lastname': lastname,
        'email': email, 
        'posts': posts,
        'path': path,
        'points': points
    }
    template = loader.get_template('blog/profile.html')
    return HttpResponse(template.render(context, request))

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
    
    numComentarios = 0
    post = get_object_or_404(Posts, pk=id)
    cur = connection.cursor()
    cur.callproc('commentsPost', [id,])
    comentarios = cur.fetchall()
    
    cur.nextset()
    cur.callproc('numCommentPost', [id,])
    num = cur.fetchall()
    
    cur.nextset()
    cur.callproc('addViewPost', [id,])
    
    cur.close 
    template = loader.get_template('blogClient/PostNoticias.html')
    

    if num != ():
        numComentarios = num[0][1]

    context = {
    'post': post,
    'comentarios': comentarios,
    'id': id,
    'numComentarios': numComentarios
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
    user = int(request.session['Usuario'])
    cur.callproc('EGSP_InsertComment', [comment, user, id,])
    cur.close
    context = {}
    #return redirect('postNoticias', id=idk)
    return HttpResponseRedirect(reverse('blog:postNoticias', args=[id])) 
    

def insertPost(request):
    print("Entra a insert post")
    template = loader.get_template('blog/newNoticia.html')
    title = request.POST.get('title')
    comment = request.POST.get('comment')
    content = request.POST.get('content')
    user = int(request.session['Usuario'])
    cur = connection.cursor()
    cur.callproc('EInsertPost', [title, comment, content, user])
    cur.close
    return HttpResponseRedirect(reverse('blog:noticias')) 
    
def updateUser(request):
    template = loader.get_template('blog/profile.html')
    
    user = int(request.session['Usuario'])
    idTipoUsuario = int(request.session['IdTipoUsuario'])

    username = request.POST.get('username')
    lastname = request.POST.get('lastname')
    email =  request.POST.get('email')
    password = request.POST.get('password')

    cur = connection.cursor()
    cur.callproc('EGSP_UpdateUser', [user, username, lastname, email, password, idTipoUsuario])
    cur.close

    return HttpResponseRedirect(reverse('blog:Perfil'))
