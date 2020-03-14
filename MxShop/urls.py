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
from django.conf.urls import url
# from django.contrib import admin
import xadmin
# from django.urls import path
from apps.users import views
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
    # url(r'test',view=views.test)
    # path('admin/', admin.site.urls)
]