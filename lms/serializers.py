from django.contrib.auth.models import User
from rest_framework import serializers
from lms.models import Product, Lesson, ProductAccess


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class ProductsToBuyListSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(read_only=True,
                                             source='lesson_set.count')  # выводим количество уроков на курсе
    students_count = serializers.SerializerMethodField()  # выводим количество студентов на курсе

    class Meta:
        model = Product
        fields = ('title', 'start_date', 'price', 'lessons_count', 'students_count')

    def get_students_count(self, obj):
        """Получаем количество студентов на курсе"""
        product_access_list = ProductAccess.objects.filter(product=obj)
        return User.objects.filter(productaccess__in=product_access_list).count()


class AvailableProductsListSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(read_only=True, source='lesson_set.count')

    class Meta:
        model = Product
        fields = ('id', 'title', 'start_date', 'lessons_count')
