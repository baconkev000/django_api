from django.shortcuts import render

from PIL import Image, ImageOps

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dogs_api.models import DogInfo
from dogs_api.serializers import DogsInfoSerializer
import requests

import urllib.request

# Gets a list of all dogs
class DogInfoList(APIView):
    """
    Returns a list of all dogs in the database. Contains: dog breed, image of dog, and grayscale image of dog
    """
    def get(self, request):
        
        if DogInfo.objects.all().count() != 24:
            add_dogs()

        dogs = DogInfo.objects.all()
        serializer = DogsInfoSerializer(dogs, many=True)
        return Response(serializer.data)

class DogImagesMod(APIView):
    """
    Returns a single dog from the database. Must be specified by id number.
     Contains: dog breed, image of dog, and grayscale image of dog
    """
    def get(self, request, pk):
        if DogInfo.objects.all().count() != 24:
            add_dogs()

        dog = DogInfo.objects.get(id=pk)
        serialzer = DogsInfoSerializer(dog)

        return Response(serialzer.data, status=status.HTTP_200_OK)

# Populates db with dog objects from 3rd party Dog API
def add_dogs():

    root = 'http://localhost:8000'
    path = '/media/images/'
    urlPath = root + path

    # turns response into usable data and creates new dog objects
    r = requests.get('https://dog.ceo/api/breeds/image/random/24')
    urls = r.json()['message']

    for x in urls:

        breedName = x.split('/')[4]
        imgName = breedName + '.jpg'
        urllib.request.urlretrieve(x, 'media/images/' + imgName)

        org_path = urlPath + imgName
        mod_path = urlPath + 'mod/' + imgName

        # create a grayscale/modded version of the original dog image and store it in the mod images folder
        img = Image.open('.' + path + imgName)
        gray_img = ImageOps.grayscale(img)
        gray_img.save('./media/images/mod/' + imgName)

        newDog = DogInfo(breed=breedName, org_img=org_path, mod_img=mod_path)
        
        newDog.save()