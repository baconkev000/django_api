from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

import requests


# Create your views here.
class DogsAPIInfo(APIView):
    
    def get(self, request):
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        return Response(response)
    