from django.urls import path

from . import views

urlpatterns = [
    path('',views.feed,name='feed'),
    path('createPost',views.createPost,name='createPost'),
    path('createComment', views.createComment, name='createComment')
]