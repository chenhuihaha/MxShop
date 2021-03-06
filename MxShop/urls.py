"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views_base import GoodsListView
from goods.views import GoodsListViewSet, CategoryViewset
from users.views import SmsCodeViewset, UserViewset

router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsListViewSet, basename='goods')

# 配置category的url
router.register(r'categorys', CategoryViewset, basename='categorys')

router.register(r'code', SmsCodeViewset, basename='code')

router.register('users',UserViewset,basename='users')
goods_list = GoodsListViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    # url(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # 商品列表页
    # url(r'goods/$', goods_list, name='goods-list'),
    url(r'^', include(router.urls)),
    url(r'docs/', include_docs_urls(title='慕学生鲜')),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),

    # jwt认证接口
    url(r'^login/', obtain_jwt_token),

]
