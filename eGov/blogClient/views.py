from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Comments, Posts
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
from django.core.urlresolvers import reverse



def newProject(request):
    return render(request, 'blogClient/newProyecto.html')

def newNoticia(request):
    return render(request, 'blogClient/newNoticia.html')

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

    template = loader.get_template('blogClient/noticias.html')

    cur = connection.cursor()
    cur.callproc('selectNewsClient', [])
    noticias = cur.fetchall()
    cur.close
    


    print(noticias)
    context = {
        'noticias': noticias 
    }
    return HttpResponse(template.render(context, request))


def Proyectos(request):
    template = loader.get_template('blogClient/proyectos.html')
    
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
    mBotonAgrPunto = ""
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

    
    print(points)
    print(comentarios)
    

    cur.close 
    template = loader.get_template('blogClient/PostNoticias.html')
    
    if points == ():
        resultado = "Mostrar"


    if num != ():
        numComentarios = num[0][1]

    if user != userElements[0][0]:
        mBotonAgrPunto = "Mostrar"


    
    context = {
    'post': post,
    'comentarios': comentarios,
    'id': id,
    'numComentarios': numComentarios,
    'resultado': resultado,
    'userElements': userElements[0],
    'mBotonAgrPunto': mBotonAgrPunto,
    }
    return HttpResponse(template.render(context, request))

def ProyectosDetail(request, id):
    
    numComentarios = 0
    resultado = ""
    user = int(request.session['Usuario'])
    post = get_object_or_404(Posts, pk=id)
    template = loader.get_template('blogClient/PostProyectos.html')
    

    cur = connection.cursor()
    cur.callproc('commentsPost', [id,])
    comentarios = cur.fetchall()
    
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


    
    cur.close

    Path = comentarios[0][3]
    
    if votes != ():
        resultado = "Mostrar"


    if num != ():
        numComentarios = num[0][1]

    
    


    context = {
    'post': post,
    'comentarios': comentarios,
    'numComentarios': numComentarios,
    'id': id,
    'estadisticas': estadisticas[0],
    'resultado': resultado,
    'Path': Path,
    'userElements': userElements[0],
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
    
def insertCommentProject(request, id):

    template = loader.get_template('blogClient/PostNoticias.html')
    comment = request.POST.get('comment')
    cur = connection.cursor()
    user = int(request.session['Usuario'])
    cur.callproc('EGSP_InsertComment', [comment, user, id,])
    cur.close
    context = {}
	 
    return HttpResponseRedirect(reverse('blogClient:postProyectos', args=[id])) 

def insertPost(request):
    template = loader.get_template('blogClient/newNoticia.html')
    title = request.POST.get('title')
    comment = request.POST.get('comment')
    content = request.POST.get('content')
    user = int(request.session['Usuario'])
    cur = connection.cursor()
    cur.callproc('EInsertPost', [title, comment, content, user])
    cur.close
    return HttpResponseRedirect(reverse('blogClient:noticias')) 
    

def updateUser(request):
    template = loader.get_template('blogClient/profile.html')
    
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
    
    template = loader.get_template('blogClient/editarNoticia.html')
    context = {
        'id': id
    }
    return HttpResponse(template.render(context, request))


def editarNoticiaEsp(request, id):

    template = loader.get_template('blogClient/editarNoticia.html')
    title = request.POST.get('title')
    comment = request.POST.get('description')
    content = request.POST.get('content')

    cur = connection.cursor()
    cur.callproc('updatePost', [id, title, comment, content])
    cur.close
    return HttpResponseRedirect(reverse('blogClient:Perfil'))

def deletePost(request, id):

    template = loader.get_template('blogClient/profile.html')
    context = {}
    cur = connection.cursor()
    cur.callproc('deletePost', [id])
    cur.close

    return HttpResponseRedirect(reverse('blogClient:Perfil'))


def ProyectoAddYes(request, id):
    user = int(request.session['Usuario'])
        
    cur = connection.cursor()
    cur.callproc('addYesProject', [id])

    cur.nextset()
    cur.callproc('InsertVotePost', [user, id,])
    

    cur.close


    return HttpResponseRedirect(reverse('blogClient:postProyectos', args=[id]))
    
    
def NoticiaAddOne(request, id):
    user = int(request.session['Usuario'])
        
    cur = connection.cursor()
    cur.callproc('getUserPost', [id])
    userC = cur.fetchall()
    userE = userC[0][0]
    

    cur.nextset()
    cur.callproc('addPointUser', [userE])

    cur.nextset()
    cur.callproc('InsertPointPost', [user, id,])
    

    cur.close


    return HttpResponseRedirect(reverse('blogClient:postNoticias', args=[id])) 
    

def ProyectoAddNo(request, id):
    user = int(request.session['Usuario'])
    
    cur = connection.cursor()
    cur.callproc('addNoProject', [id])

    cur.nextset()
    cur.callproc('InsertVotePost', [user, id,])
    
    cur.close

    return HttpResponseRedirect(reverse('blogClient:postProyectos', args=[id])) 
    

def ProyectoAddUnknown(request, id):
    
    user = int(request.session['Usuario'])
    
    cur = connection.cursor()
    cur.callproc('addUnknownProject', [id])

    cur.nextset()
    cur.callproc('InsertVotePost', [user, id,])
    
    cur.close

    return HttpResponseRedirect(reverse('blogClient:postProyectos', args=[id])) 
    

