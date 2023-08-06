import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")

app = Celery("myapp")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "run-every-10-seconds": {
        "task": "myapp.tasks.foo",
        "schedule": timedelta(seconds=10),
    },
    "run-every-1800-seconds": {
        "task": "myapp.tasks.bar",
        "schedule": timedelta(seconds=1800),
    },
}
