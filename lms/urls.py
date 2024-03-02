from django.urls import path
from lms.views import ProductListAPIView, LessonListView, AvailableProductListAPIView

urlpatterns = [
    path('products-to-buy/', ProductListAPIView.as_view(), name='product-list'),
    path('product/<int:product_id>/lessons/', LessonListView.as_view(), name='lesson-list'),
    path('products/available/', AvailableProductListAPIView.as_view(), name='available-product-list'),
]

