from django.urls import path
from .import views


app_name = 'farm'

urlpatterns =[
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
]