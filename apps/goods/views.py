from django.shortcuts import render
# from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination  # 分页功能
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Goods,GoodsCategory
from .filters import GoodstFilter
from .serializers import GoodsSerializer,CategorySerializer



# Create your views here.

# drf的modelserializer实现商品列表页功能
# class GoodsListView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#
#     def get(self, request, format=None):
#         print(111)
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 自定义分页
class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_parm = 'p'
    max_page_size = 100


# GenericView方式实现商品列表页和分页功能
# class GoodsListView(generics.ListAPIView):
#     """
#     商品列表页
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination

# def get(self, request, *args, **kwargs):
#     return self.list(request, *args, **kwargs)


# viewsets和router完成商品列表页
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """商品列表页,分页，搜索，过滤，排序"""
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodstFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')


class CategoryViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
