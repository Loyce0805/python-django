from django.urls import path
from myapp import views


urlpatterns = [
    path('show', views.showFunc),
]