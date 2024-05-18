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
        serializers = PlacesSerializer(places,many=True)
        return Response(serializers.data,status.HTTP_200_OK)
    
    def post(self,request,format=None):
        # 新しい場所の作成
        serializer = PlacesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Successfully created a new location!"},HTTP_200_OK)
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
            serializer = PlacesSerializer(place, data=request.data)
            if serializer.is_valid:
                # リクエストのデータに含まれるフィールドを更新
                if 'name' in data:
                    place.name = data['name']
                if 'memo' in data:
                    place.memo = data['memo']
                if 'address' in data:
                    place.address = data['address']
                if 'image_url' in data:
                    place.image_url = data['image_url']
                if 'updated_at' in data:
                    place.updated_at = data['updated_at']
                place.save()
                serializer = PlacesSerializer(place)
                return Response(serializer.data,status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Places.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

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
        return Response(status.HTTP_200_OK)

class FoldersViewId(APIView):
    def get(self, request, folder_id):
        return Response(status.HTTP_200_OK)