from django.test import TestCase
from accounts.forms import RegisterForm, SignInForm
from django.contrib.auth.models import User

class TestAccountForm(TestCase):

    def test_register_form(self):
        form = RegisterForm(data={
            'email': 'test@gmail.com',
            'username': 'testuser24',
            'password1': 'Justatest123',
            'password2': 'Justatest123'
        })

        self.assertTrue(form.is_valid())

    def test_register_form_invalid(self):
        form = RegisterForm(data={
            'email': 'test@gmail.com',
            'username': 'testuser24',
            'password1': 'Justatest12',
            'password2': 'Justatest123'
        })

        self.assertFalse(form.is_valid())
    
    def test_register_form_no_data(self):
        form = RegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)

    def test_signIn_form(self):
        user = User.objects.create_user(username='testuser',password='justatest12')
        form = SignInForm(data={
            'username': 'testuser',
            'password': 'justatest12'
        })

        self.assertTrue(form.is_valid())

    def test_sigIn_form_invalid(self):
        user = User.objects.create_user(username='testuser',password='justatest12')
        form = SignInForm(data={
            'username': 'testuse',
            'password': 'justatest12'
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)

    def test_signIn_form_no_data(self):
        user = User.objects.create_user(username='testuser',password='justatest12')
        form = SignInForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)