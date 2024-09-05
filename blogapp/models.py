from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=250)
    tag=models.CharField(max_length=250)
    #body=models.TextField()
    body=RichTextField(blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    blog_datetime=models.DateTimeField(auto_now_add=True)
    thumbnail=models.ImageField(null=True,blank=True,upload_to="images/")
    category=models.CharField(max_length=250,default='uncategorized')

    def __str__(self):
        return self.title+' | '+str(self.author)
    
    def get_absolute_url(self):
        return reverse('article',args=(str(self.id)))


'''class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    p_p=models.ImageField()

    def __str__(self):
        return self.user.username
'''    
class Category(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
