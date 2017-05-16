from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Comments, Posts
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
from django.core.urlresolvers import reverse

def index(request):
    
    print("ENTRE")
    template = loader.get_template('home/inicio.html')
    context = {}
    

    return HttpResponse(template.render(context, request))



def login(request):

    template = loader.get_template('home/header.html')
    context = {}
    
    username = request.POST.get('username')
    password = str(request.POST.get('password'))
    cur = connection.cursor()
    login = cur.callproc('login', [username, password])
    login = cur.fetchall()
    cur.close
    print(login)
    request.session['Usuario'] = login[0][0]
    request.session['TipoUsuario'] = login[0][1]
    request.session['IdTipoUsuario'] = login[0][2]
    
    if login[0][1] == "Administrador":
        return HttpResponseRedirect(reverse('blog:noticias'))
    elif login[0][1] == "Cliente":
        print("ENTRSLKDS A CLIENTKADSD")
        return HttpResponseRedirect(reverse('blogClient:noticias'))

def signin(request):
    
    template = loader.get_template('home/header.html')
    context = {}
    
    name = request.POST.get('name')
    lastname = str(request.POST.get('lastname'))
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = str(request.POST.get('password'))
    cur = connection.cursor()
    cur.callproc('SignIn', [name, lastname, username, email, password,])
    cur.fetchall()
    cur.nextset()

    
    login = cur.callproc('login', [username, password])
    login = cur.fetchall()
    cur.close
   
    request.session['Usuario'] = login[0][0]
    request.session['TipoUsuario'] = login[0][1]
    request.session['IdTipoUsuario'] = login[0][2]
    
    return HttpResponseRedirect(reverse('blogClient:noticias'))
    

    
    
def redirectNoticias(request):
    
    template = loader.get_template('home/header.html')
    
    if request.session['TipoUsuario'] == "Administrador":
        return HttpResponseRedirect(reverse('blog:noticias'))

    elif request.session['TipoUsuario'] == "Cliente":
        return HttpResponseRedirect(reverse('blogClient:noticias'))

def redirectProyectos(request):
    
    template = loader.get_template('home/header.html')
    
    if request.session['TipoUsuario'] == "Administrador":
        return HttpResponseRedirect(reverse('blog:proyectos'))

    elif request.session['TipoUsuario'] == "Cliente":
        return HttpResponseRedirect(reverse('blogClient:proyectos'))

def redirectPerfil(request):
    
    template = loader.get_template('home/header.html')
    
    print(request.session['TipoUsuario'])
    if request.session['TipoUsuario'] == "Administrador":
        return HttpResponseRedirect(reverse('blog:Perfil'))

    elif request.session['TipoUsuario'] == "Cliente":
        return HttpResponseRedirect(reverse('blogClient:Perfil'))
    
    
def salir(request):

    template = loader.get_template('home/header.html')
    
    del request.session['Usuario']
    del request.session['TipoUsuario']
    del request.session['IdTipoUsuario']

    request.session.modified = True

    return HttpResponseRedirect(reverse('personal:contact'))
