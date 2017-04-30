from django.conf.urls import url

from . import views


app_name = 'appeGov'
urlpatterns = [

    #/appeGov/
    url(r'^$', views.index, name='index'),

    #/appeGov/numero/
    url(r'^(?P<pic_id>[0-9]+)/$', views.profilepic, name='profilepic'),

    url(r'^profilepicform/$', views.profilepicform, name='profilepicform'),

    url(r'^profilepicFormA/$', views.profilepicFormA, name='profilepicFormA'),
]
