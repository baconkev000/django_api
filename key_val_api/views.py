from sqlite3 import IntegrityError

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework.schemas import AutoSchema

from .models import KeyVal
from .serializers import KeyValueSerializer

# Create your views here.
class KeyValueList(APIView):
    """
    Returns a list of all key/value pairs.
    """
    # gets all objects and returns usable data
    def get(self, request):
        keys = KeyVal.objects.all()
        serializer = KeyValueSerializer(keys, many=True)        

        return Response(serializer.data)

class CreateKeyVal(APIView):
    """
    Creates a key value pair. Specify name of key in request body. Values are default set to 0.
    """
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
    """
    Returns the information of any specified key name.
    """
    # gets and returns the data of the requested key
    def get(self, request, keyName):
        currentKey = KeyVal.objects.get(key=keyName)
        serializer = KeyValueSerializer(currentKey)
        return Response(serializer.data)

class IncrementKeyVal(APIView):
    """
    Increments the value of any specified key.
    Note: value is only increased by 1.
    """
    # increments val of specified key by specified num
    def put(self, request, keyName):
        key = KeyVal.objects.get(key=keyName)
        
        try:
            key.val = key.val + 1
            key.save()

            serializer = KeyValueSerializer(key)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class KeyValDeleteByKeyName(APIView):
    """
    Deletes any key/val pair. Must be specified by key name.
    """
    # deletes a specified key/val pair by name
    def delete(self, request, keyName):
        try: 
            allKeys = KeyVal.objects.all()
            key = KeyVal.objects.get(key=keyName)
            key.delete()
            serializer = KeyValueSerializer(allKeys)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)