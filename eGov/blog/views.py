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
    
    

    cur.nextset()
    cur.callproc('PostsXUser', [user,])
    posts = cur.fetchall()
    
    cur.close
    
    print(posts)
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
    
    template = loader.get_template('blog/noticias.html')

    cur = connection.cursor()
    cur.callproc('selectNewsAdmin', [])
    noticias = cur.fetchall()
    cur.close
    


    print(noticias)
    context = {
    	'noticias': noticias 
    }
    return HttpResponse(template.render(context, request))

def Proyectos(request):
    
    template = loader.get_template('blog/proyectos.html')
	
    cur = connection.cursor()
    cur.callproc('selectLawProjects', [])
    proyectos = cur.fetchall()
    cur.close
    
    
    
    context = {
    	'proyectos': proyectos 
    }
    return HttpResponse(template.render(context, request))



def NoticiasDetail(request, id):
    numComentarios = 0
    resultado = ""
    user = int(request.session['Usuario'])
    post = get_object_or_404(Posts, pk=id)
    cur = connection.cursor()
    cur.callproc('commentsPost', [id,])
    comentarios = cur.fetchall()
        
    
    cur.nextset()
    cur.callproc('numCommentPost', [id,])
    num = cur.fetchall()

    cur.nextset()
    cur.callproc('addViewPost', [id,])

    cur.nextset()
    cur.callproc('getPointPost', [user, id,])
    points = cur.fetchall()


    cur.nextset()
    cur.callproc('getUserPost', [id,])
    userElements = cur.fetchall()
    
    cur.close 
    template = loader.get_template('blog/PostNoticias.html')
    

    if num != ():
        numComentarios = num[0][1]

    
    if user != userElements[0][0]:
        resultado = "Mostrar"

    print(comentarios)
    context = {
    'post': post,
    'comentarios': comentarios,
    'id': id,
    'numComentarios': numComentarios,
    'resultado': resultado,
    'userElements': userElements[0],
    }
    return HttpResponse(template.render(context, request))

def ProyectosDetail(request, id):
    numComentarios = 0
    
    resultado = ""
    user = int(request.session['Usuario'])
    
    post = get_object_or_404(Posts, pk=id)
    template = loader.get_template('blog/PostProyectos.html')
    

    cur = connection.cursor()
    cur.callproc('commentsPost', [id,])
    comentarios = cur.fetchall()
    
    cur.nextset()

    cur.callproc('getLinkLawProject', [id,])
    link = cur.fetchall()

    print(link)

    cur.nextset()

    
    cur.callproc('numCommentPost', [id,])
    num = cur.fetchall()
    
    cur.nextset()
    cur.callproc('addViewPost', [id,])

    cur.nextset()
    cur.callproc('getStadisticsProject', [id,])
    estadisticas = cur.fetchall()

    cur.nextset()
    cur.callproc('getVotePost', [user, id,])
    votes = cur.fetchall()

    cur.nextset()
    cur.callproc('getUserPost', [id,])
    userElements = cur.fetchall()

    print("POST")
    
    if votes != ():
        resultado = "Mostrar"

    if num != ():
        numComentarios = num[0][1]

    linkE = ""

    if link != ():
        linkE = link[0][0]

    Path = comentarios[0][3]

    context = {
    'post': post,
    'comentarios': comentarios,
    'id': id,
    'numComentarios': numComentarios,
    'estadisticas': estadisticas[0],
    'resultado': resultado,
    'Path': Path,
    'userElements': userElements[0],
    'linkE':linkE
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
	 
    return HttpResponseRedirect(reverse('blog:postNoticias', args=[id])) 
	
def insertCommentProject(request, id):

    template = loader.get_template('blog/PostNoticias.html')
    comment = request.POST.get('comment')
    cur = connection.cursor()
    user = int(request.session['Usuario'])
    cur.callproc('EGSP_InsertComment', [comment, user, id,])
    cur.close
    context = {}
	 
    return HttpResponseRedirect(reverse('blog:postProyectos', args=[id])) 
    

def insertPost(request):
    template = loader.get_template('blog/newNoticia.html')
    title = request.POST.get('title')
    comment = request.POST.get('comment')
    content = request.POST.get('content')
    user = int(request.session['Usuario'])
    cur = connection.cursor()
    cur.callproc('EInsertPostAdmin', [title, comment, content, user])
    cur.close
    return HttpResponseRedirect(reverse('blog:noticias')) 


def insertProject(request):
    template = loader.get_template('blog/newNoticia.html')
    title = request.POST.get('title')
    comment = request.POST.get('comment')
    content = request.POST.get('content')
    link = request.POST.get('link')

    user = int(request.session['Usuario'])
    
    cur = connection.cursor()
    cur.callproc('EInsertPostAdmin', [title, comment, content, user])
    
    cur.nextset()
    
    cur.callproc('selectLastPost', [])
    Post = cur.fetchall()
    idPost = int(Post[0][0])
    
    cur.nextset()

    cur.callproc('EInsertLawProject', [idPost, link])
    
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

    return HttpResponseRedirect(reverse('blog:Perfil'))


def ProyectoAddYes(request, id):
    
    user = int(request.session['Usuario'])
    
    cur = connection.cursor()
    cur.callproc('addYesProject', [id])

    cur.nextset()
    cur.callproc('InsertVotePost', [user, id,])

    cur.close


    return HttpResponseRedirect(reverse('blog:postProyectos', args=[id])) 
    

def ProyectoAddNo(request, id):
    
    user = int(request.session['Usuario'])
    

    cur = connection.cursor()
    cur.callproc('addNoProject', [id])

    cur.nextset()
    cur.callproc('InsertVotePost', [user, id,])

    cur.close

    return HttpResponseRedirect(reverse('blog:postProyectos', args=[id])) 
    

def ProyectoAddUnknown(request, id):
    
    user = int(request.session['Usuario'])
    
    
    cur = connection.cursor()
    cur.callproc('addUnknownProject', [id])

    cur.nextset()
    cur.callproc('InsertVotePost', [user, id,])

    cur.close

    return HttpResponseRedirect(reverse('blog:postProyectos', args=[id])) 


def aceptarNoticia(request, id):

    cur = connection.cursor()
    cur.callproc('acceptNew', [id])
    cur.close

    return HttpResponseRedirect(reverse('blog:noticias'))

def rechazarNoticia(request, id):

    cur = connection.cursor()
    cur.callproc('rejectNew', [id])
    cur.close

    return HttpResponseRedirect(reverse('blog:noticias'))
