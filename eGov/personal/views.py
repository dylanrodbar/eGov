from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
from django.core.urlresolvers import reverse

from smtplib import SMTP
#import smtplib

def contact(request):
    return render(request, 'personal/contact.html')



def enviarCorreo(request):

    template = loader.get_template('personal/contact.html')
    
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    email = request.POST.get('email')
    telefono = request.POST.get('telefono')
    mensaje = request.POST.get('mensaje')
    passwordE = request.POST.get('password')

    mensajeE = ''
    mensajeE += 'Nombre: ' + nombre + '\n'
    mensajeE += 'Apellido: ' + apellido + '\n'
    mensajeE += 'Telefono: ' + telefono + '\n'
    mensajeE += mensaje + '\n'
    
    destino = "egov881@gmail.com"
    asunto = "necesito contactar"

    EnviarCorreo = SMTP()
    EnviarCorreo.connect("smtp.gmail.com", 587)
    EnviarCorreo.starttls()
    EnviarCorreo.ehlo()
    EnviarCorreo.login(email, passwordE)

    Cabecera = 'To:' + destino + '\n'     
    Cabecera += 'From: ' + email + '\n'
    Cabecera += 'Subject: ' + asunto + '\n'+'\n'

    EnviarCorreo.sendmail(email, destino, Cabecera + mensajeE)

    EnviarCorreo.close()
    
 

    return HttpResponseRedirect(reverse('personal:contact'))
    
    
    
