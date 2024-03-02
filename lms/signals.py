from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from lms.models import Group, ProductAccess


@receiver(post_save, sender=ProductAccess)
def distribute_user_to_group(sender, instance, created, **kwargs):
    if created:
        product = instance.product  # получаем выбранный продукт
        user = instance.student  # получаем выбранного пользователя
        groups = product.group_product.all()  # получаем все группы продукта

        if product.start_date > timezone.now():
            if not groups.exists():
                group = Group.objects.create(product=product,
                                             title=f'{product.title}-Group-1')  # создаем новую группу, если еще нет
                group.students.add(user)
            else:
                # Распределяем студентов в группы с наименьшим числом участников
                min_group = min(groups, key=lambda x: x.students.count())
                if min_group.students.count() < product.maximum_students:
                    min_group.students.add(user)
                else:
                    # Создаем новую группу если существующая заполнена до максимума
                    group = Group.objects.create(product=product, title=f'{product.title}-Group-{groups.count() + 1}')
                    group.students.add(user)
