from rest_framework import serializers
from .models import DogInfo

class DogsInfoSerializer(serializers.ModelSerializer):
    breed = serializers.CharField()
    org_img = serializers.CharField()
    mod_img = serializers.CharField()

    class Meta:
        # specifies what information is shown in the api response -- __all__ shows all info
        model = DogInfo
        fields = '__all__'
