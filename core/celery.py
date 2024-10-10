from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

# Defina o módulo de configurações padrão do Django para o programa 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Usar uma string aqui significa que o trabalhador não precisa serializar
# o objeto de configuração para processos filhos.
# - namespace='CELERY' significa todas as chaves de configuração relacionadas ao celery
# deve ter um prefixo `CELERY_`.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_connection_retry_on_startup = True

# Carregue módulos de tarefas de todos os aplicativos Django registrados.
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')