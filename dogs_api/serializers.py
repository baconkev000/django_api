from wsgiref import validate
from rest_framework import serializers
from .models import DogInfo

class DogsInfoSerializer(serializers.ModelSerializer):
    breed = serializers.CharField()
    url = serializers.CharField()

    class Meta:
        # specifies what information is shown in the api response -- __all__ shows all info
        model = DogInfo
        fields = '__all__'