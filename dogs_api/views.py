from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dogs_api.models import DogInfo
from dogs_api.serializers import DogsInfoSerializer
import requests
import json

def add_dogs():
    r = requests.get('https://dog.ceo/api/breeds/image/random/24')
    urls = r.json()["message"]

    for x in urls:
        breedName = x.split("/")[4]
        newDog = DogInfo(breed=breedName, url=x)
        newDog.save()

class DogInfoList(APIView):
    def get(self, request):
        if DogInfo.objects.all().count() != 24:
            add_dogs()

        dogs = DogInfo.objects.all()
        serializer = DogsInfoSerializer(dogs, many=True)
        return Response(serializer.data)

class DogImagesMod(APIView):
    pass
        



# Populate db with dog responses from Dog API
# Get all dog objects and return 1