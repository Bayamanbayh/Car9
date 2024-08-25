from django.urls import path
from .views import *


urlpatterns = [
    path('', CarViewSet.as_view({'get': 'list',
                                     'post': 'create'}), name='product_list'),
    path('<int:pk>/', CarViewSet.as_view({'get': 'retrieve',
                                            'put': 'update',
                                            'delete': 'destroy'}), name='product_detail'),
    path('category/', MarkaViewSet.as_view({'get': 'list',
                                     'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', MarkaViewSet.as_view({'get': 'retrieve',
                                            'put': 'update',
                                            'delete': 'destroy'}), name='category_detail'),
]