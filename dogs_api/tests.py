from curses import keyname
from django.test import TestCase
import os, os.path

from .models import DogInfo
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from .views import add_dogs

class DogInfoTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('dogs/', include('dogs_api.urls')),
    ]

    # The add_dogs function will create 48 new dog images every time tests is run
    # Every test clears the db afterwards, but does not clear the media folder of images
    # Therefore, to avaoid an unneccessary amount of images, both unit tests are in this one function
    def test_add_dogs_and_get_single_dog(self):
        # TESTING ADD DOGS - asserting that the add dogs function adds 24 dog objects exactly
       # add_dogs()
       # self.assertEqual(DogInfo.objects.all().count(), 24)
       # self.assertNotEqual(DogInfo.objects.all().count(), 2)

        # TESTING GET SINGLE DOG - asserting that the get request returns two dog image urls
       # url = reverse('dog-info', kwargs={'pk':'1'})
       # response = self.client.get(url)
        
       # self.assertEqual(response.status_code, status.HTTP_200_OK)
       # self.assertIsNotNone(DogInfo.objects.get(id=1).breed)
       # self.assertIsNotNone(DogInfo.objects.get(id=1).org_img)
       # self.assertIsNotNone(DogInfo.objects.get(id=1).mod_img)
       pass
    

