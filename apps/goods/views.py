from django.shortcuts import render
from rest_framework import status

from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Goods


# Create your views here.
class GoodsListView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        print(111)
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    def post(self, request, format=None):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
