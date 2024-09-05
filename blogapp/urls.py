from django.urls import path
from .views import *


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about/',AboutView,name='about'),
    path('article/<int:pk>',ArticleDetail.as_view(),name='article'),
    path('post/',AddPostView.as_view(),name='addpost'),
    path('aritcle/edit/<int:pk>',EditPost.as_view(),name='editpost'),
    path('aritcle/<int:pk>/delete',DeletePost.as_view(),name='deletepost'),
]