from contextlib import nullcontext
from curses import keyname
from django.test import TestCase

from .models import DogInfo
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from .views import add_dogs

class DogInfoTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('dogs/', include('dogs_api.urls')),
    ]

    # asserting that the add_dogs function creates exactly 24 dog objects
    def test_add_dogs(self):
        add_dogs()

        self.assertEqual(DogInfo.objects.all().count(), 24)
        self.assertNotEqual(DogInfo.objects.all().count(), 2)

    # asserting that the get api is not failing
    def test_get_all_dogs_objects(self):
        url = reverse('list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(DogInfo.objects.all().count(), 24)

    def test_has_dog_images(self):
        url = reverse('images-res', kwargs={'pk':'1'})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    