from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """Модель продукта"""
    title = models.CharField(max_length=255, verbose_name='Название')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость')
    minimum_students = models.IntegerField(verbose_name='Минимальное количество студентов группы')
    maximum_students = models.IntegerField(verbose_name='Максимальное количество студентов группы')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductAccess(models.Model):
    """Модель проверки доступа к продукту у студента"""
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Студент')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    is_active = models.BooleanField(default=True, verbose_name='Доступ')

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.product.title}"

    class Meta:
        verbose_name = 'Доступ'
        verbose_name_plural = 'Доступы'


class Lesson(models.Model):
    """Модель урока"""
    title = models.CharField(max_length=255, verbose_name='Название')
    video_url = models.URLField(verbose_name='Ссылка на видео')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Group(models.Model):
    """Модель группы студентов на курсе"""
    title = models.CharField(max_length=255, verbose_name='Название')
    students = models.ManyToManyField(User, related_name='group', verbose_name='Ученики', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='group_product', verbose_name='Продукт')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
