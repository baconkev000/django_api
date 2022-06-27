from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dogs_api.models import DogInfo
from django.urls import include, path, reverse
import requests
import random

def index(request):
    url = 'http://localhost:8000/dogs'

    response= requests.get(url).json()
    template = loader.get_template('how_to/index.html')

    randomInt = random.randint(1, 24)
    context = {
        'response':response,
        'randInt': randomInt
    }
    return HttpResponse(template.render(context, request))

def howto_keyval(request):
    url = 'http://localhost:8000/dogs'

    response= requests.get(url).json()
    template = loader.get_template('how_to/keyval.html')

    context = {
        'response':response,
    }
    return HttpResponse(template.render(context, request))