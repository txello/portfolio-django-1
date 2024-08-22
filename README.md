# Система Задач - Django RTF+Celery

## Установка

```console
pip install django-admin djangorestframework celery redis
```

Если вы используете Windows, установите дополнительно:
```console
pip install eventlet
```

Также установите нужные приложения:
* RabbitMQ
* Celery
* Redis-server

## Запуск

### Django:
```console
py manage.py runserver
```

### Также перед запуском Django, запустите приложения, указанные выше

### Celery:
```console
celery -A myproject worker -l info
```

#### ... или Windows:
```console
celery -A myproject worker -l info -P eventlet
```

## Описание

Проект содержит базу данных, состоящих из `Проекты` и `Задачи`. Для каждого проекта можно создать задачу и пользователя для него.\
Пользователь же указывается через стандартного пользователя `Django`.

Используется `Django-RTF`.

`Celery` используется для отправки уведомления о создании новой задачи на почту создателя проекта.\
Для `Celery` используется `RabbitMQ`+`Redis`.\
Настройки `Celery` указываются в `settings.py`, сам экземпляр класса хранится в `celery.py` и запускается через `__init__.py`
