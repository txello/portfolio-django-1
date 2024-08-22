from celery import shared_task
from django.core.mail import send_mail
from .models import Task

@shared_task
def send_task_created_notification(task_id):
    try:
        task = Task.objects.get(id=task_id)
        subject = f'Новая задача: {task.title}'
        message = f'Задача "{task.title}" была создана в проекте "{task.project.name}".\n' \
                  f'Описание: {task.description}\n' \
                  f'Дедлайн: {task.due_date}\n' \
                  f'Исполнитель: {task.assigned_to.username if task.assigned_to else "Не назначен"}'
        recipient_list = [task.assigned_to.email] if task.assigned_to else []

        if recipient_list:
            print(task.project.owner.email)
            send_mail(subject, message, task.project.owner.email, recipient_list)
    except Task.DoesNotExist:
        print(f'Задача с ID {task_id} не найдена.')
