from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('dodaj/', views.pizza, name='pizza'),
]