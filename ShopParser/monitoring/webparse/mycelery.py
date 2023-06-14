from celery import Celery

# Создание экземпляра Celery
app = Celery('webparse')

# Загрузка настроек из переменной окружения
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач
app.autodiscover_tasks()
