from django.db import models

class Post(models.Model):
    title= models.CharField(max_length=140)
    description= models.TextField()
    content= models.TextField()
    date= models.DateTimeField()
    user= models.CharField(max_length=140)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
     user= models.CharField(max_length=140)
     date= models.DateTimeField()
     description= models.TextField()
     post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True) 

     def __str__(self):
        return '%s %s %s' % (self.user,self.date.self.description)

    
    
