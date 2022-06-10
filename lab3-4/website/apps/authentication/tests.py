from django.test import TestCase
from .models import User


class TestUser(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('test_user', email=None, password='testpass')

    def test_get_user(self):
        user = User.objects.get(username='test_user')
        self.assertTrue(user.check_password('testpass'))

    def test_login(self):
        login = self.client.login(username='test_user', password='testpass')
        self.client.logout()

    def test_logout(self):
        response = self.client.get(f'/logout')
        self.assertEqual(response.status_code, 200)