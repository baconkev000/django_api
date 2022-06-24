from http.client import HTTPResponse
from this import s
from django.shortcuts import render

from PIL import Image, ImageEnhance
from io import BytesIO

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dogs_api.models import DogInfo
from dogs_api.serializers import DogsInfoSerializer
import requests

import json
import urllib.request

# Gets all dog objects

class DogInfoList(APIView):
    def get(self, request):
        if DogInfo.objects.all().count() != 24:
            add_dogs()

        dogs = DogInfo.objects.all()
        serializer = DogsInfoSerializer(dogs, many=True)
        return Response(serializer.data)

class DogImagesMod(APIView):
    def get(self, request, pk):
        dog = DogInfo.objects.get(id=pk)

        if DogInfo.objects.all().count() == 24:
            add_dogs()
        
        img = Image.open(dog.org_img)
        dog.org_img = img.convert('L')
        img.save('grayscale.jpg')

        dog.save()

        serialzer = DogsInfoSerializer(dog)


        return Response(serialzer.data)

# Populates db with dog objects from 3rd party Dog API
def add_dogs():

# turns response into usable data and creates new dog objects
    r = requests.get('https://dog.ceo/api/breeds/image/random/24')
    urls = r.json()["message"]

    for x in urls:

        breedName = x.split("/")[4]
        urllib.request.urlretrieve(x, "media/" + breedName + ".jpg")
        response = requests.get(x)
        img_data = Image.open(BytesIO(response.content))

        newDog = DogInfo(breed=breedName, org_img=x, mod_img=img_data)
        
        newDog.save()