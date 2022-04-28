'''
Created on 2022. 4. 28.

'''
# 메인 urls의 위임
from django.urls import path
from myguest import views

urlpatterns = [
    path('', views.ListFunc),
    path('insert', views.InsertFunc),
    path('insertok', views.InsertOkFunc)
]