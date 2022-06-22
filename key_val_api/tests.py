from curses import keyname
from django.test import TestCase

from .models import KeyVal
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

class KeyValTasts(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('keyval/', include('key_val_api.urls')),
    ]

    # asserting get api
    def test_get_kv(self):
        url = reverse('list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # asserting that the post api is posting correct key and vals and returning correct status codes
    def test_post_kv(self):
        url = reverse('list')
        response = self.client.post(url, {'key':'Test Post', 'val':'1'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(KeyVal.objects.all().count(), 1)
        self.assertEqual(KeyVal.objects.get(id=1).key, 'Test Post')
        self.assertEqual(KeyVal.objects.get(id=1).val, 1)

        response = self.client.post(url, {'key':'Test Post', 'val':'hello'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # asserting that the put api is incrementing the val of the specified key
    def test_post_kv(self):
        url = reverse('kv-detail')

        self.client.post(url, {'key':'Test Post', 'val':'1'}, format='json')

        response = self.client.put(url, {'key':'Test Put', 'inc':'1'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(KeyVal.objects.get(id=1).val, 2)


