from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import path, include

from book.models import Book


class BooksTests(APITestCase, URLPatternsTestCase):

    urlpatterns = [
        path('api/', include('book.urls')),
    ]

    def test_create_book(self):
        """
        Ensure we can create a new book object.
        """
        url = 'http://localhost:8000/api/book/'
        data = {
            "title": "test",
            "publisher": "test",
            "author": "Author",
            "pages": 123,
            "tags": "['test', 'test2']"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'test')

        url = f'http://localhost:8000/api/book/{Book.objects.get().id}/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'test')

        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'test')
