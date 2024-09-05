from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from django.urls import reverse_lazy
from .forms import PostForm

# Create your views here.

#def home(request):
#    return render(request,'home.html',{})

class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering=['-blog_datetime']


class ArticleDetail(DetailView):
    model=Post
    template_name='articledet.html'

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='addpost.html'
    #fields='__all__'

class AddCategoryView(CreateView):
    model=Category
    #form_class=PostForm
    template_name='addcategory.html'
    fields='__all__'

class EditPost(UpdateView):
    model=Post
    form_class=PostForm
    template_name='editpost.html'
    #fields=['title','tag','body']

class DeletePost(DeleteView):
    model=Post
    template_name='deletepost.html'
    success_url=reverse_lazy('home')


def AboutView(request):
    return render(request,'about.html')

