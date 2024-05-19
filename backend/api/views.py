from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Folders, Places
from .serializers import FoldersSerializer, PlacesSerializer
from rest_framework import status

class PlacesView(APIView):
    # 場所に関する関数
    def get(self,request,format=None):
        # 場所の一覧を取得する、一覧取得
        places = Places.objects.all()
        name = request.GET.get('name','')
        created_at = request.GET.get('created_at','') # クエリパラメータの取得、初期値は空文字
        if name:
            places = places.filter(name=name)
        if created_at:
            places = places.filter(created_at=created_at)
        serializers = PlacesSerializer(places,many=True)
        return Response(serializers.data,status.HTTP_200_OK)
    
    def post(self,request,format=None):
        # 新しい場所の作成
        serializer = PlacesSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Successfully created a new location!"},status.HTTP_200_OK)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class PlacesViewID(APIView):
    # 場所のIDを使用した関数
    def get(self,request,place_id):
        # IDで指定した場所を取得
        try:
            place = Places.objects.get(id=place_id)
            serializer = PlacesSerializer(place)
            return Response(serializer.data, status.HTTP_200_OK)
        except Places.DoesNotExist:
            return Response({"detail": "Place not found"},status.HTTP_404_NOT_FOUND)
   
    def put(self,request,place_id):
        # IDで指定したの（場所の名前の変更 or メモを変更 or 住所を変更 or 画像を変更 or updated_atに日付を追加）
        # 変更した項目ごとにHTTPレスポンスの内容を変更する
        try:
            place = Places.objects.get(id=place_id)
            serializer = PlacesSerializer(place, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message":"Successfully updated!"},status.HTTP_200_OK)
        except Places.DoesNotExist:
            return Response({"detail": "Place not found"},status.HTTP_404_NOT_FOUND)

    def delete(self,request,place_id):
        # IDで指定した場所を削除
        try:
            place = Places.objects.get(id=place_id)
            place.delete()
            return Response(status.HTTP_204_NO_CONTENT)
        except Places.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

class FoldersView(APIView):
    def get(self, request):
        folders = Folders.objects.all()
        name = request.GET.get('name', '')
        created_at = request.GET.get('created_at', '')
        
        if name:
            folders = folders.filter(name=name)
        if created_at:
            folders = folders.filter(created_at=created_at)
        
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
