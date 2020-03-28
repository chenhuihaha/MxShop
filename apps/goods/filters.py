import django_filters
from .models import Goods

class GoodstFilter(django_filters.rest_framework.FilterSet):
    """商品过滤类"""
    price_min = django_filters.NumberFilter(field_name='shop_price',lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')


    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']