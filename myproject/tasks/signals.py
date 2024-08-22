from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from .tasks import send_task_created_notification

@receiver(post_save, sender=Task)
def task_created(sender, instance, created, **kwargs):
    if created:
        send_task_created_notification.delay(instance.id)