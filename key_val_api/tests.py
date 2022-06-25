from curses import keyname
from socket import timeout
import time
from django.test import TestCase

from .models import KeyVal
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

keyName = 'testKey'
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
        url = reverse('create-keyval')
        response = self.client.post(url, {'key':keyName, 'val':'1'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(KeyVal.objects.all().count(), 1)
        self.assertEqual(KeyVal.objects.get(key=keyName).val, 0)

    def test_disallow_empty_key(self):
        url = reverse('create-keyval')
        response = self.client.post(url, {'key':''}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    # asserting that it is not possible to create duplicate keys
    #def test_disallow_duplicate_key(self):
     #   url = reverse('create-keyval')
      #  response = self.client.post(url, {'key':'Test Post', 'val':'1'}, format='json')

       # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #response = self.client.post(url, {'key':'Test Post', 'val':'1'}, format='json')
        #self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    # asserting taht the put request only accepts an inc param which increments the keys val
    def test_update_val_of_key(self):
        url = reverse('create-keyval')
        response = self.client.post(url, {'key':keyName, 'val':'1'}, format='json')

        url = reverse('update-key', kwargs={'keyName':keyName})
        response = self.client.put(url, {'inc': '1'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(KeyVal.objects.get(key=keyName).val, 1)

        response = self.client.put(url, {'inc': 'string'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.put(url, {'key':keyName, 'inc': 'string'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # asserting that the delete api is deleting the specified key
    def test_delete_keybyname_val(self):
        url = reverse('create-keyval')
        response = self.client.post(url, {'key':keyName}, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(KeyVal.objects.all().count(), 1)

        url = reverse('deletekey', kwargs={'keyName':keyName})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(KeyVal.objects.all().count(), 0)
       

    #def test_multiple_requests(self):
    #    url = reverse('create-keyval')
    #    for x in range(10000):
    #        keyNumName = str(x)
    #        self.client.post(url, {'key':keyNumName , 'val':'1'}, format='json')
        
    #    self.assertEqual(KeyVal.objects.all().count(), 10000)