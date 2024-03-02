# LMS-backend-django (тестовое задание)

Проект backend системы обучения


## Технологии:

[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/) [![Django Rest Framework](https://img.shields.io/badge/-Django_Rest_Framework-092E20?style=flat)](https://www.django-rest-framework.org/)
[![API](https://img.shields.io/badge/-API-4CAF50?style=flat)](https://en.wikipedia.org/wiki/Application_programming_interface)
[![Swagger](https://img.shields.io/badge/-Swagger-85EA2D?style=flat&logo=swagger&logoColor=white)](https://swagger.io/)

## Описание:

Проект представляет сущности для создания системы обучения, lms.
Создается продукт/курс, уроки, подтверждение доступа пользователя к курсу, уроки на курсе.
Логика работы наполнения групп студентами следующая:
- администратор выдает доступ на курс пользователю
- если групп в курсе не существует, в момент выдачи доступа автоматически формируется первая группа и в нее записывается студент
- последующие студенты которым выдается доступ укомплектовывают доступную группу до максимально заданного значения
- при условии укомплектованности группы, автоматически создается новая группа
В проекте реализованы следующие эндпоинты:
- ```http://localhost:8000/api/products-to-buy/``` - выводит список доступных для покупки продутов, если пользователь прошел базовую авторизацию выводит для студента только не купленные продукты
- ```http://localhost:8000/api/products/available/``` - выводит список купленых студентом продуктов
- ```http://localhost:8000/api//product/{product_id}/lessons/``` - ```{product_id}``` - номер продукта, выводит список уроков конкретного продукта


## Установка:

- Для начала работы с проектом клонируйте репозиторий:
    - ```git clone https://github.com/NickolayBabulich/LMS-backend-django.git```
- Перейти в папку проекта, установить виртуальное окружение ```python -m venv venv```
- Установить зависимости ```pip install -r requirements.txt```
- Подготовить миграции ```python manage.py makemigrations```
- Провести миграции ```python manage.py migrate```
- Запустить проект командой ```docker compose up```
- Загрузить тестовые данные при необходимости:
  - ```python manage.py loaddata users.json``` - загрузка данных администратора и студентов
  - ```python manage.py loaddata lms-data.json``` - загрузка данных с продуктами
- Запустить сервер ```python manage.py runserver```

## Дополнительно:
- Для управления сущностями авторизуйтесь под администратором ```http://localhost:8000/admin/```
  - логин администратора: ```admin```
  - пароль администратора: ```1```
- Документация по эндпоинтам доступна по ссылке ```http://localhost:8000/swagger/```
- У всех студентов задан пароль ```1```, логины студентов возможно увидеть в админке либо в ```lms-data.json```