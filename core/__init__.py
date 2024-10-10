# Isso garantirá que o aplicativo seja sempre importado quando
# O Django iniciar para que shared_task use este aplicativo.
from .celery import app as celery_app

__all__ = ('celery_app',)