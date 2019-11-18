from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Post, Comment

# Create your views here.
def feed(request):
    # Check if user is sign in
    if request.user.is_authenticated:
        # Get all posts and comments
        posts = Post.objects.all()
        comments = Comment.objects.all()
        context = {
            'posts': posts,
            'comments': comments,
        }
        return render(request, 'feed/feed.html', context)
    else:
        return redirect('signIn')


# Create a post
def createPost(request):
    if request.method == "POST" and request.user.is_authenticated:
        # Get Form data
        text = request.POST['post']
        user = request.user
        post = Post(text=text,author=user)
        post.save()
        messages.success(request,'Your post has been added')
        return redirect('feed')
    else:
        messages.error('user is not authenticated')
        return redirect('feed')


# Create a comment
def createComment(request):
    if request.method == "POST" and request.user.is_authenticated:
        # Get required data for a comment
        author = request.user
        text = request.POST['comment']
        # Make sure comment does not exceed char limit
        if(len(text) >= 150):
            messages.error(request, 'Your comment exceeds 150 characters')
            return redirect('feed')
        post_id = int(request.POST['post_id'])
        # Get post and save new comment object in database
        post = get_object_or_404(Post, pk=post_id)
        comment = Comment(author=author,text=text,post=post)
        comment.save()
        messages.success(request,'Your comment has been added')
        return redirect('feed')
    else:
        messages.error('user is not authenticated')
        return redirect('signIn')



