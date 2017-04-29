from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader


from .models import Image, Post, Profilepicture, Stadistic, Tag, Tagsxpost, User, Usertype

# Create your views here.

def index(request):
    latest_question_list = Profilepicture.objects.all()[:6]
    template = loader.get_template('appeGov/index.html')
    context = {
        'latest_question_list': latest_question_list, #se referencia la variable que usará el .html
    }
    return HttpResponse(template.render(context, request))


def profilepic(request, pic_id):
    #try:
    pic = get_object_or_404(Profilepicture, pk=pic_id)
        #pic = Profilepicture.objects.get(id=pic_id)
    template = loader.get_template('appeGov/pic.html')
    context = {
        'pic': pic
    }
    
    #except Profilepicture.DoesNotExist:
    #    raise Http404("Picture does not exist")

    return HttpResponse(template.render(context, request))
