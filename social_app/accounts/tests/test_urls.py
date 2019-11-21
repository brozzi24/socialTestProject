from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import register, signIn, signOut

class TestAccountUrls(SimpleTestCase):

    # Test URLS use the correct view
    def test_register_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func,register)
    
    def test_signIn_url(self):
        url = reverse('signIn')
        self.assertEquals(resolve(url).func,signIn)

    def test_signOut_url(self):
        url = reverse('signOut')
        self.assertEquals(resolve(url).func,signOut)

    
