from pyexpat import model

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import KeyVal
from .serializers import KeyValueSerializer

# Create your views here.
class KeyValueList(APIView):

    # gets all objects and returns usable data
    def get(self, request):
        keys = KeyVal.objects.all()
        serializer = KeyValueSerializer(keys, many=True)
        return Response(serializer.data)

    # takes request arg and trys to post -- response status is either created or erro
    def post(self, request):
        serializer = KeyValueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class KeyValueDetail(APIView):
    
    # gets and returns the data of the requested key
    def get(self, request, keyParam):
        currentKey = KeyVal.objects.get(key=keyParam)
        serializer = KeyValueSerializer(currentKey)
        return Response(serializer.data)

    # increments val of specified key by specified num
    def put(self, request, keyParam):
        key = KeyVal.objects.get(key=keyParam)
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

    
class KeyValueDelete(APIView):

    # deletes a specified key/val pair
    def delete(self, request, keyParam):
        key = KeyVal.objects.get(key=keyParam)
        key.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
