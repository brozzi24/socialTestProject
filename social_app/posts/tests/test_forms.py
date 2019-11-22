from django.test import SimpleTestCase
from posts.forms import postForm, commentForm


class TestForm(SimpleTestCase):
    def test_post_form(self):
        form = postForm(data={"text": "Mason Rudolph started it"})

        self.assertTrue(form.is_valid())

    def test_post_form_no_data(self):
        form = postForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_comment_form(self):
        form = commentForm(data={"text": "Free Myles Garrett"})

        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        form = commentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
