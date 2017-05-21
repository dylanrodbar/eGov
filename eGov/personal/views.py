from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
from django.core.urlresolvers import reverse

import smtplib


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
    mensajeE += 'Nombre: ' + nombre + ''
    mensajeE += 'Apellido: ' + apellido + ''
    mensajeE += 'Telefono: ' + telefono + ''
    mensajeE += mensaje + ''
    
    asunto = "Solicitud de contacto"


    fromaddr = email
    toaddrs  = 'egov881@gmail.com'
    msg = mensajeE

    print(msg)
    
 
    # Datos
    username = email
    password = passwordE
 
    # Enviando el correo
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs,  msg)
    server.quit()

    return HttpResponseRedirect(reverse('personal:contact'))
    
    
    
