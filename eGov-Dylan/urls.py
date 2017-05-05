from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    url(r'^appeGov/', include('appeGov.urls')), #include: para referenciar otras configuraciones de URL
    url(r'^admin/', admin.site.urls),
]
