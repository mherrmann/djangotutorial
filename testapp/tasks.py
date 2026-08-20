from celery import shared_task
@shared_task
def beat_task():
    return 'beat-works-djevopstest1787206200'