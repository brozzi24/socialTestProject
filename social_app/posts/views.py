from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from .models import Post, Comment
from . import forms

# Create your views here.


def feed(request):
    # Check if user is sign in
    if request.user.is_authenticated:
        # Get all posts and comments
        posts = Post.objects.all()
        comments = Comment.objects.all()
        comment_count = Comment.objects.count()

        # Get user id for delete
        user_id = request.user.id

        # Get Forms
        postForm = forms.postForm
        commentForm = forms.commentForm
        context = {
            "posts": posts,
            "comments": comments,
            "comment_count": comment_count,
            "user_id": user_id,
            "postForm": postForm,
            "commentForm": commentForm,
        }
        return render(request, "feed/feed.html", context)
    else:
        return redirect("signIn")


# Create a post
def createPost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # Get form
            form = forms.postForm(request.POST)

            # Check if form is valid
            if form.is_valid():
                text = form.cleaned_data["text"]
                author = request.user
                post = Post(text=text, author=author)
                post.save()
                messages.success(request, "Your post has been posted!")

                # Send email to let users know of new post
                users = User.objects.all()
                user_email_list = []

                # Loop through users to alert new post
                for user in users:
                    # Don't send email to creater of post
                    if user.email != author.email:
                        user_email_list.append(user.email)

                # Check user email list is not empty
                if user_email_list:
                    send_mail(
                        "New Post!",
                        '{} has created a new post: \n "{}"'.format(
                            author.username, text
                        ),
                        "no-reply@testproject.com",
                        set(user_email_list),
                        fail_silently=False,
                    )

                return redirect("feed")
            else:
                messages.error(request, "Post is not valid")
                return redirect("feed")
        else:
            messages.error(request, "Post was not submitted properly")
            return HttpResponseRedirect("/")
    else:
        messages.error(request, "You must be signed in to create a post")
        return redirect("signIn")


# Delete a post
def deletePost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # Get form data
            post_id = int(request.POST["post_id"])

            # Query database for post with post_id
            post = Post.objects.filter(id=post_id)
            post.delete()
            messages.success(request, "Post has been deleted")
            return redirect("feed")
        else:
            messages.error(request,'You select a post to delete')
            return redirect("feed")
    else:
        messages.error(request,'You must be signed in to delete a post')
        return redirect("signIn")


# Create a comment
def createComment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # Get form
            form = forms.commentForm(request.POST)

            # Check if form is valid
            if form.is_valid():
                # Get form data and user/post
                text = form.cleaned_data["text"]
                author = request.user

                # Get post
                post_id = request.POST["post_id"]
                post = get_object_or_404(Post, pk=post_id)

                # Create and save comment to database
                comment = Comment(text=text, author=author, post=post)
                comment.save()
                messages.success(request, "You comment has been added")
                return redirect("feed")
            else:
                messages.error(request, "Comment is not valid")
                return redirect("feed")
        else:
            messages.error(
                request, "You must fill out a comment box on a post to submit comment"
            )
            return HttpResponseRedirect("/")
    else:
        messages.error(request, "user is not authenticated")
        return redirect("signIn")


def deleteComment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # Get form data
            comment_id = request.POST["comment_id"]

            # Query database for post with post_id
            comment = Comment.objects.filter(id=comment_id)
            comment.delete()
            messages.success(request, "Comment has been deleted")
            return redirect("feed")
        else:
            messages.error(request,'You select a comment to delete')
            return redirect("feed")
    else:
        messages.error(request, 'You must be signed in to delete a comment')
        return redirect("signIn")
