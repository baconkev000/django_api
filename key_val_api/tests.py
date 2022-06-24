from curses import keyname
from django.test import TestCase

from .models import KeyVal
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

class KeyValTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('keyval/', include('key_val_api.urls')),
    ]

    # asserting that the get api is not failing
    def test_get_all_key_vals(self):
        url = reverse('list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # asserting that the post api is posting correct key and vals and returning correct status codes
    # post should only create a key and default value of 0
    # post should return HTTP 400 if key is empty
    def test_create_key_val(self):
        url = reverse('create')

        response = self.client.post(url, {'key':'Test Post', 'val':'1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(KeyVal.objects.all().count(), 1)
        self.assertEqual(KeyVal.objects.get(id=1).key, 'Test Post')
        self.assertEqual(KeyVal.objects.get(id=1).val, 0)

        response = self.client.post(url, {'key':''}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    # asserting taht the put request only accepts an inc param which increments the keys val
    def test_update_val_of_key(self):
        url = reverse('update-key')
        response = self.client.post(url, {'key':'Test-Put', 'val':'1'}, format='json')

        url = reverse('kv-detail', kwargs={'keyParam':'Test-Put'})

        response = self.client.put(url, {'inc': '1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(KeyVal.objects.get(key='Test-Put').val, 1)

        response = self.client.put(url, {'inc': 'string'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.put(url, {'key':'Test-Put', 'inc': 'string'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # asserting that the delete api is deleting the specified key
    def test_delete_key_val(self):
        url = reverse('deletekey')

        response = self.client.post(url, {'key':'Test-Del'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(KeyVal.objects.all().count(), 1)

        url = reverse('deletepk', kwargs={'keyParam':'Test-Del'})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(KeyVal.objects.all().count(), 0)