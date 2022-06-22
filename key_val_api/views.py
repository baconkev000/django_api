from pyexpat import model
from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from .models import KeyVal
from .serializers import KeyValueSerializer

import coreapi

class KeyValueSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('key')
            ]

            manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


# Create your views here.
class KeyValueList(APIView):

    schema = KeyValueSchema

    # simply gets all objects and returns usable data
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

    schema = KeyValueSchema
    
    def delete(self, request, pk):
        key = KeyVal.objects.get(id=pk)
        key.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # takes two args from request -- key and inc (incrementing number)
    def put(self, request, pk):
        key = KeyVal.objects.get(id=pk)
        # serializer transforms data in to usable code and then we update the 
        serializer = KeyValueSerializer(key, data=request.data)
        if serializer.is_valid():
            serializer.val = serializer.val + 1
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)