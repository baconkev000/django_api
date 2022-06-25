from curses import keyname
from pyexpat import model
from sqlite3 import IntegrityError
from django.views.generic.detail import DetailView

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import coreapi

from .models import KeyVal
from .serializers import KeyValueSerializer

# Create your views here.
class KeyValueList(APIView):
    # gets all objects and returns usable data
    def get(self, request):
        keys = KeyVal.objects.all()
        serializer = KeyValueSerializer(keys, many=True)

        return Response(serializer.data)


class CreateKeyVal(APIView):
    # takes request arg and trys to post -- response status is either created or erro
    def post(self, request):
        try:
            serializer = KeyValueSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class GetKeyVal(APIView):
    # gets and returns the data of the requested key
    def get(self, request, keyName):
        currentKey = KeyVal.objects.get(key=keyName)
        serializer = KeyValueSerializer(currentKey)
        return Response(serializer.data)

class IncrementKeyVal(APIView):
    # increments val of specified key by specified num
    def put(self, request, keyName):
        key = KeyVal.objects.get(key=keyName)
        data = request.data
        
        try:
            key.val = key.val + int(data['inc'])
            key.save()

            serializer = KeyValueSerializer(key)
            return Response(serializer.data)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
class KeyValDeleteByKeyName(APIView):
    # deletes a specified key/val pair by name
    def get(self, request, keyName):
        currentKey = KeyVal.objects.get(key=keyName)
        serializer = KeyValueSerializer(currentKey)
        return Response(serializer.data)

    def delete(self, request, keyName):
        try: 
            key = KeyVal.objects.get(key=keyName)
            key.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
