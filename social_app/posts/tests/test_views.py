from django.test import TestCase, Client
from django.urls import reverse
from posts.models import Post, Comment
from posts.views import feed
from django.contrib.auth.models import User, auth

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',password='brandon24')
        self.post1 = Post.objects.create(author=self.user,text='Do you know what they call a quarter pounder in europe?')
        self.feed_url = reverse('feed')
        self.createPost = reverse('createPost')
        self.deletePost = reverse('deletePost')
        self.createComment = reverse('createComment')
        self.deleteComment = reverse('deleteComment')
        
        

    """
        FEED VIEW
    """
    # Check response is 200 and correct template is used
    def test_feed_view_signed_in(self):
        login = self.client.login(username='testuser', password='brandon24')
        response = self.client.get(self.feed_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'feed/feed.html')

    # Check user gets redirected if not sign in
    def test_feed_view_signed_out(self):
        self.client.logout()
        response = self.client.get(self.feed_url)

        self.assertRedirects(response, '/accounts/signIn', status_code=302)

    """
        CREATE POST VIEW
    """
    # Create post with valid form and user signed in
    def test_createPost_valid(self):
        post_count = Post.objects.count()
        login = self.client.login(username='testuser',password='brandon24')
        response = self.client.post(self.createPost, data={
            'text': 'be alot cooler if you did',
        })

        self.assertEquals(Post.objects.count(), post_count+1)
        self.assertRedirects(response, '/', status_code=302)

    # Create post with invalid form data
    def test_createPost_invalid_form(self):
        post_count = Post.objects.count()
        login = self.client.login(username='testuser',password='brandon24')
        response = self.client.post(self.createPost)

        self.assertEquals(Post.objects.count(),post_count)
        self.assertRedirects(response, '/', status_code=302)

    # User is not signed in
    def test_createPost_user_logged_out(self):
        post_count = Post.objects.count()
        response = self.client.post(self.createPost, data={
            'text': 'be alot cooler if you did',
        })

        self.assertEquals(Post.objects.count(), post_count)
        self.assertRedirects(response, '/accounts/signIn', status_code=302)

    """
        DELETE POST
    """
    # Test if user is not signed in
    def test_deletePost_user_logged_out(self):
        post_count = Post.objects.count()

        response = self.client.post(self.deletePost)

        self.assertEquals(Post.objects.count(), post_count)
        self.assertRedirects(response, '/accounts/signIn', status_code=302)

    # Form is not post method
    def test_deletePost_user_not_post(self):
        post_count = Post.objects.count()
        login = self.client.login(username='testuser',password='brandon24')

        response = self.client.get(self.deletePost)

        self.assertEquals(Post.objects.count(), post_count)
        self.assertRedirects(response, '/', status_code=302)
       
    # Everything is valid
    def test_deletePost(self):
        post2 = Post.objects.create(author=self.user,text='hello')
        post_count = Post.objects.count()
        login = self.client.login(username='testuser',password='brandon24')

        response = self.client.post(self.deletePost, data={
            'post_id': post2.id,
        })
        

        self.assertEquals(Post.objects.count(), post_count-1)
        self.assertRedirects(response, '/', status_code=302)

    """
            CREATE COMMENT
    """

    # Create Comment with valid form and user signed in
    def test_createComment_valid(self):
        comment_count = Comment.objects.count()
        login = self.client.login(username='testuser',password='brandon24')
        response = self.client.post(self.createComment, data={
            'text': 'be alot cooler if you did',
            'post_id': self.post1.id,
        })
        self.assertRedirects(response, '/', status_code=302)
        self.assertEquals(Comment.objects.count(), comment_count+1)

    # Create Comment with invalid form data
    def test_createComment_invalid_form(self):
        comment_count = Comment.objects.count()
        login = self.client.login(username='testuser',password='brandon24')
        response = self.client.post(self.createComment)

        self.assertEquals(Comment.objects.count(),comment_count)
        self.assertRedirects(response, '/', status_code=302)

    # # User is not signed in
    def test_createComment_user_logged_out(self):
        comment_count = Comment.objects.count()
        response = self.client.post(self.createComment, data={
            'text': 'be alot cooler if you did',
        })

        self.assertEquals(Comment.objects.count(), comment_count)
        self.assertRedirects(response, '/accounts/signIn', status_code=302)

       
    """
        DELETE COMMENT
    """
    # Test if user is not signed in
    def test_deleteComment_user_logged_out(self):
        comment_count = Comment.objects.count()

        response = self.client.post(self.deleteComment)

        self.assertEquals(Comment.objects.count(), comment_count)
        self.assertRedirects(response, '/accounts/signIn', status_code=302)

    # Form is not post method
    def test_deleteComment_user_not_post(self):
        comment_count = Comment.objects.count()
        login = self.client.login(username='testuser',password='brandon24')

        response = self.client.get(self.deleteComment)

        self.assertEquals(Comment.objects.count(), comment_count)
        self.assertRedirects(response, '/', status_code=302)
       
    # Everything is valid
    def test_deleteComment(self):
        comment = Comment.objects.create(author=self.user,text='hello',post=self.post1)
        comment_count = Comment.objects.count()
        login = self.client.login(username='testuser',password='brandon24')

        response = self.client.post(self.deleteComment, data={
            'comment_id': comment.id,
        })
        

        self.assertEquals(Comment.objects.count(), comment_count-1)
        self.assertRedirects(response, '/', status_code=302)