from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
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
        author = request.user
        post = Post(text=text,author=author)
        post.save()
        messages.success(request,'Your post has been added')
        # Send email to let users know of new post
        users = User.objects.all()
        user_email_list = []
        for user in users:
            # Don't send email to creater of post
            if user.email != author.email:
                user_email_list.append(user.email)
        # Check user email list is not empty 
        if user_email_list:
            send_mail(
                'New Post!',
                '{} has created a new post: \n {}'.format(author.username, text),
                'no-reply@testproject.com',
                user_email_list,
                fail_silently=False,
            )
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



