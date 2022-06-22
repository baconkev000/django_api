from rest_framework import serializers
from .models import KeyVal

class KeyValueSerializer(serializers.ModelSerializer):
    class Meta:
        # specifies what information is shown in the api response -- __all__ shows all info
        model = KeyVal
        fields = '__all__'
