from django.test import TestCase
from django.urls import reverse


class UserRegisterViewTests(TestCase):
    def test_user_register_view(self):
        response = self.client.get(reverse('user:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/register.html')


class UserLoginViewTests(TestCase):
    def test_user_login_view(self):
        response = self.client.get(reverse('user:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')


class UserLogoutViewTests(TestCase):
    def test_user_logout_view(self):
        response = self.client.get(reverse('user:logout'))
        self.assertEqual(response.status_code, 302)
