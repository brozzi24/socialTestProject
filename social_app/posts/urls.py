from django.urls import path

from . import views

urlpatterns = [
    path('',views.feed,name='feed'),
    path('createPost',views.createPost,name='createPost'),
    path('createComment', views.createComment, name='createComment'),
    path('deletePost',views.deletePost, name='deletePost'),
    path('deleteComment',views.deleteComment, name='deleteComment'),
]