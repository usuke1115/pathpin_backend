from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Folders, Places
#from serializers import 
from rest_framework import status

class PlacesView(APIView):
    # 場所に関する関数
    def get(self,request,format=None):
        # 場所の一覧を取得する、一覧取得
        return Response(status.HTTP_200_OK)
    """
    def post(self,request,format=None):
        # 新しい場所の作成
        pass
    """


class PlacesViewID(APIView):
    # 場所のIDを使用した関数
    def get(self,request,id):
        # IDで指定した場所を取得
        pass

"""
    
    def put(self,request,id):
        # IDで指定したの（場所の名前の変更 or メモを変更　or 住所を変更　or 画像を変更 or updated_atに日付を追加）
        # 変更した項目ごとにHTTPレスポンスの内容を変更する
        pass
    
    def delete(self,request,id):
        # IDで指定した場所を削除
        pass

"""