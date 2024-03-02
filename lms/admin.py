from django.contrib import admin
from lms.models import Product, ProductAccess, Lesson, Group


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'price', 'minimum_students', 'maximum_students', 'owner')


@admin.register(ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'product', 'is_active')

    def student_name(self, obj):
        return f'{obj.student.first_name} {obj.student.last_name}'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'product')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')
