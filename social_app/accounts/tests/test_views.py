from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth


class TestAccountViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse("register")
        self.signIn_url = reverse("signIn")
        self.signOut_url = reverse("signOut")
        self.user = User.objects.create_user(username="testuser", password="justatest")

    """
            REGISTER VIEW
    """
    # User not signed in
    def test_register_not_signed_in(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")

    # User is signed in
    def test_register_signed_in(self):
        login = self.client.login(username="testuser", password="justatest")
        response = self.client.get(self.register_url)

        self.assertRedirects(response, "/", status_code=302)

    # Requst is post and with valid form data
    def test_register_valid_form(self):
        user_count = User.objects.count()
        response = self.client.post(
            self.register_url,
            {
                "email": "jedi@force.com",
                "username": "babyyoda24",
                "password1": "testthisis",
                "password2": "testthisis",
            },
        )

        self.assertRedirects(response, "/accounts/signIn", status_code=302)

    # Request is post and with invalid form data
    def test_register_invalid_form(self):
        user_count = User.objects.count()
        response = self.client.post(
            self.register_url,
            {
                "email": "jedi@force.com",
                "username": "babyyoda24",
                "password1": "testthisis",
                "password2": "faildYouHave",
            },
        )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")

    """
            SIGNIN VIEW
    """

    def test_signIn_already_signed_in(self):
        login = self.client.login(username="testuser", password="justatest")
        response = self.client.get(self.signIn_url)

        self.assertRedirects(response, "/", status_code=302)

    # User is not logged in and form data is valid
    def test_signIn_valid_form(self):
        response = self.client.post(
            self.signIn_url, {"username": "testuser", "password": "justatest",}
        )
        user = auth.get_user(self.client)
        self.assertEquals(self.user, user)
        self.assertRedirects(response, "/", status_code=302)

    # User form invalid
    def test_signIn_invalid_form(self):
        response = self.client.post(
            self.signIn_url, {"username": "testuser", "username": "wrongpassword",}
        )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/signIn.html")

    """
            SIGNOUT VIEW
    """
    # User is logged in then gets signed out
    def test_signOut_user(self):
        login = self.client.login(username="testuser", password="justatest")
        response = self.client.get(self.signOut_url)
        user = auth.get_user(self.client)

        self.assertNotEqual(self.user, user)
        self.assertRedirects(response, "/accounts/signIn", status_code=302)

    # User is not logged in
    def test_signOut_not_signed_in(self):
        response = self.client.get(self.signOut_url)

        self.assertRedirects(response, "/accounts/signIn", status_code=302)
