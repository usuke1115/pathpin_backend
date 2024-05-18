from rest_framework import serializers

from .models import Folders, Places

class FoldersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folders
        fields = '__all__'

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = '__all__'