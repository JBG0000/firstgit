"""lionproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from blog.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name="home"), #메인 페이지
    path('blog/', include('blog.urls')), #home 페이지에서 다른 html로 분기할 때 blog/가 앞에 붙음
    path('account/', include('account.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #<- static를 병렬적으로 추가해준다 : 미디어를 계속 새로 추가될때마다 붙여넣기? 해준다 url분기????
