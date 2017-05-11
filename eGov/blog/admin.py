from django.contrib import admin
from blog.models import Post
from blog.models import Comment
from blog.models import User

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)

