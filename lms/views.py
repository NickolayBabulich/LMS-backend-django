from rest_framework import generics
from rest_framework.permissions import AllowAny

from lms.models import Product, Lesson, ProductAccess
from lms.serializers import ProductsToBuyListSerializer, AvailableProductsListSerializer, LessonListSerializer


class AvailableProductListAPIView(generics.ListAPIView):
    """Отрисовка приобретенных студентом продуктов"""
    queryset = Product.objects.all()
    serializer_class = AvailableProductsListSerializer

    def get_queryset(self):
        user = self.request.user
        purchased_product_id = ProductAccess.objects.filter(student=user, is_active=True).values_list('product_id',
                                                                                                      flat=True)
        return Product.objects.filter(id__in=purchased_product_id)


class ProductListAPIView(generics.ListAPIView):
    """Отрисовка доступных для приобретения продуктов"""
    queryset = Product.objects.all()
    serializer_class = ProductsToBuyListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            purchased_product_id = ProductAccess.objects.filter(student=user, is_active=True).values_list('product_id',
                                                                                                          flat=True)
            return Product.objects.exclude(id__in=purchased_product_id)
        else:
            return Product.objects.all()


class LessonListView(generics.ListAPIView):
    """Отрисовка доступных уроков для конкретного продукта"""
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        product_access = ProductAccess.objects.filter(student=user, product_id=product_id, is_active=True)
        if product_access.exists():
            return Lesson.objects.filter(product_id=product_id)
        else:
            return Lesson.objects.none()
