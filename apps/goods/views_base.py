from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过django的View实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]

        # 常规提取数据转json方法，无法转换date，image等字段
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #
        #     json_list.append(json_dict)

        # 使用model_to_dict提取数据,无法将image等字段序列化
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        # 使用serializers序列化,可以序列化所有类型的字段
        from django.core import serializers
        import json
        json_data = serializers.serialize('json',goods)
        json_data = json.loads(json_data)
        # print(type(json_data))

        from django.http import HttpResponse,JsonResponse
        return JsonResponse(json_data,safe=False)
