from django.test import TestCase
from posts.models import Post, Comment
from django.contrib.auth.models import User


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Post
        cls.user = User.objects.create_user(username="testuser", password="justatest24")
        cls.post1 = Post.objects.create(
            author=cls.user,
            text="What are your thoughts on baby yoda? #TheMandalorian",
        )
        # Comment
        cls.user2 = User.objects.create_user(
            username="testuser24", password="justatest24"
        )
        cls.comment1 = Comment.objects.create(
            author=cls.user2,
            text="I can not wait for the next episode",
            post=cls.post1,
        )

    def test_post(self):
        self.assertEquals(self.post1.author, self.user)
        self.assertEquals(
            self.post1.text, "What are your thoughts on baby yoda? #TheMandalorian"
        )

    def test_str_function(self):
        self.assertEquals(str(self.post1), "1 testuser")

    def test_comment(self):
        self.assertEquals(self.comment1.author, self.user2)
        self.assertEquals(self.comment1.text, "I can not wait for the next episode")

    def test_str_comment(self):
        self.assertEquals(str(self.comment1), "1 testuser24")
