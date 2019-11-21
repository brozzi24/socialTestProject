from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts.views import feed, createPost, createComment, deletePost, deleteComment

class TestUrls(SimpleTestCase):

    # Test URLS use the correct view
    def test_feed_url(self):
        url = reverse('feed')
        self.assertEquals(resolve(url).func,feed)

    def test_createPost_url(self):
        url = reverse('createPost')
        self.assertEquals(resolve(url).func,createPost)

    def test_createComment_url(self):
        url = reverse('createComment')
        self.assertEquals(resolve(url).func,createComment)
    
    def test_deletePost_url(self):
        url = reverse('deletePost')
        self.assertEquals(resolve(url).func,deletePost)
    
    def test_deleteComment_url(self):
        url = reverse('deleteComment')
        self.assertEquals(resolve(url).func,deleteComment)