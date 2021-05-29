from django.contrib import admin
from django.urls import path
from .views import *    #blog app의 모든 함수를 가져온다

urlpatterns = [
    path('<str:id>',detail,name="detail"),    #views 함수의 detail에서의 매개변수
    path('new/', new, name="new"),
    path('create/',create,name="create"),       #create 함수 url
    path('edit/<str:id>', edit, name = "edit"),   #id를 수정하는 창을 보여주는 기능
    path('update/<str:id>', update, name = "update"),
    path('delete/<str:id>', delete, name = "delete"),    #매개변수를 받으려면 무조건 패스 컨버터가 있어야한대
]