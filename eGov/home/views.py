from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Comments, Posts
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'home/inicio.html')


def login(request):

    username = request.POST.get('username')
    password = str(request.POST.get('password'))
    cur = connection.cursor()
    login = cur.callproc('login', [username, password])
    login = cur.fetchall()
    cur.close
    print(login[0][0])
    request.session['Usuario'] = login[0][0]
    template = loader.get_template('home/header.html')
    context = {}
    return HttpResponseRedirect(reverse('blog:noticias'))
    #return HttpResponse(template.render(context, request))        
