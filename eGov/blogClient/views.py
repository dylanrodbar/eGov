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
    print(points)

    
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
    template = loader.get_template('blogClient/profile.html')
    return HttpResponse(template.render(context, request))


template_name = 'blogClient/postProyectos.html'


def Noticias(request):
    
    template = loader.get_template('blog/noticias.html')

    cur = connection.cursor()
    cur.callproc('selectNews', [])
    noticias = cur.fetchall()
    cur.close
    


    print(noticias)
    context = {
        'noticias': noticias 
    }
    return HttpResponse(template.render(context, request))


def Proyectos(request):
    proyectos = Posts.objects.all()[:25]
    template = loader.get_template('blogClient/proyectos.html')
	
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
    template = loader.get_template('blogClient/PostProyectos.html')
    context = {
    'post': post
    }
    return HttpResponse(template.render(context, request))


def insertComment(request, id):

    template = loader.get_template('blogClient/PostNoticias.html')
    comment = request.POST.get('comment')
    cur = connection.cursor()
    user = int(request.session['Usuario'])
    cur.callproc('EGSP_InsertComment', [comment, user, id,])
    cur.close
    context = {}
    #return redirect('postNoticias', id=idk)
    return HttpResponseRedirect(reverse('blogClient:postNoticias', args=[id])) 
    

def insertPost(request):
    print("Entra a insert post")
    template = loader.get_template('blogClient/newNoticia.html')
    title = request.POST.get('title')
    comment = request.POST.get('comment')
    content = 'Contenido5'
    user = int(request.session['Usuario'])
    cur = connection.cursor()
    cur.callproc('EInsertPost', [title, comment, content, user])
    cur.close
    return HttpResponseRedirect(reverse('blogClient:noticias')) 
    

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

def editarNoticia(request, id):
    
    template = loader.get_template('blog/editarNoticia.html')
    context = {
        'id': id
    }
    return HttpResponse(template.render(context, request))


def editarNoticiaEsp(request, id):

    template = loader.get_template('blog/editarNoticia.html')
    title = request.POST.get('title')
    comment = request.POST.get('description')
    content = request.POST.get('content')

    cur = connection.cursor()
    cur.callproc('updatePost', [id, title, comment, content])
    cur.close
    return HttpResponseRedirect(reverse('blog:Perfil'))

def deletePost(request, id):

    template = loader.get_template('blog/profile.html')
    context = {}
    cur = connection.cursor()
    cur.callproc('deletePost', [id])
    cur.close

    return HttpResponseRedirect(reverse('blogClient:Perfil'))