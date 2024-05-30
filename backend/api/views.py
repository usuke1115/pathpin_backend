from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Folders, Places
from .serializers import FoldersSerializer, PlacesSerializer


class PlacesView(APIView):
    def get(self,request,format=None):
        name = request.GET.get('name', '')
        if name:
            places = Places.get_by_name(name)
            serializers = PlacesSerializer(places, many=True)
            return Response(serializers.data, status.HTTP_200_OK)
        
        created_at = request.GET.get('created_at', '')
        if created_at:
            places = Places.get_by_created_at(created_at)
            serializers = PlacesSerializer(places, many=True)
            return Response(serializers.data, status.HTTP_200_OK)
        
        places = Places.get_all()
        serializers = PlacesSerializer(places, many=True)
        return Response(serializers.data, status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = PlacesSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Successfully created a new location!"},status.HTTP_200_OK)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class PlacesViewID(APIView):
    def get(self,request,place_id):
        try:
            place = Places.objects.get(id=place_id)
            serializer = PlacesSerializer(place)
            return Response(serializer.data, status.HTTP_200_OK)
        except Places.DoesNotExist:
            return Response({"detail": "Place not found"},status.HTTP_404_NOT_FOUND)
   
    def put(self,request,place_id):
        try:
            place = Places.objects.get(id=place_id)
            serializer = PlacesSerializer(place, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message":"Successfully updated!"},status.HTTP_200_OK)
        except Places.DoesNotExist:
            return Response({"detail": "Place not found"},status.HTTP_404_NOT_FOUND)

    def delete(self,request,place_id):
        try:
            place = Places.objects.get(id=place_id)
            place.delete()
            return Response(status.HTTP_204_NO_CONTENT)
        except Places.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

class FoldersView(APIView):
    def get(self, request):
        name = request.GET.get('name', '')
        if name:
            folders = Folders.get_by_name(name)
            serializers = FoldersSerializer(folders, many=True)
            return Response(serializers.data, status.HTTP_200_OK)
        
        created_at = request.GET.get('created_at', '')
        if created_at:
            folders = Folders.get_by_created_at(created_at=created_at)
            serializers = FoldersSerializer(folders, many=True)
            return Response(serializers.data, status.HTTP_200_OK)
        
        folders = Folders.get_all()
        serializers = FoldersSerializer(folders, many=True)
        return Response(serializers.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = FoldersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ "message": "Successfully created a new folder!" }, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class FoldersViewId(APIView):
    def get(self, request, folder_id):
        try:
            folder = Folders.objects.get(id=folder_id)
            serializer = FoldersSerializer(folder)
            return Response(serializer.data, status.HTTP_200_OK)
        except Folders.DoesNotExist:
            return Response({
                "message": f"The folder with folder_id {folder_id} could not be found."
            }, status.HTTP_404_NOT_FOUND)

    def put(self, request, folder_id):
        try:
            folder = Folders.objects.get(id=folder_id)
            serializer = FoldersSerializer(folder, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        except Folders.DoesNotExist:
            return Response({
                "message": f"The folder with folder_id {folder_id} could not be found."
            }, status.HTTP_404_NOT_FOUND)

    def delete(self, request, folder_id):
        try:
            folder = Folders.objects.get(id=folder_id)
            folder.delete()
            return Response({
                "message": "Successfully created a new folder!"
            }, status.HTTP_204_NO_CONTENT)
        except Folders.DoesNotExist:
            return Response({
                "message": f"The folder with folder_id {folder_id} could not be found."
            }, status.HTTP_404_NOT_FOUND)
