from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import path, include
from django.contrib.auth.models import User


class AccountTests(APITestCase, URLPatternsTestCase):

    urlpatterns = [
        path('api/', include('auth.urls')),
    ]

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = 'http://localhost:8000/api/register/'
        data = {"email": "admin@gmail.com",
                "password": "admin"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'admin@gmail.com')
