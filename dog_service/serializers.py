from wsgiref import validate
from rest_framework import serializers
from .models import DogInfo, KeyVal

class DogInfoSerializer(serializers.ModelSerializer):
    breed = serializers.CharField(required=True, allow_blank=False, read_only=True)
    img = serializers.IntegerField(required=True, allow_blank=False, read_only=True)

    class Meta:
        # specifies what information is shown in the api response -- __all__ shows all info
        model = DogInfo
        fields = '__all__'
