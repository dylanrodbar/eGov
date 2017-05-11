from django.contrib import admin
from blog.models import Posts
from blog.models import Comments
from blog.models import Users

admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Users)

