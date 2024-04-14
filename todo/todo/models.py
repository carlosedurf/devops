from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class Task(ExportModelOperationsMixin('task'), models.Model):
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name="Título")
    description = models.TextField(null=False, blank=False, verbose_name="Descrição")
    completed = models.BooleanField(default=False, verbose_name="Feito")

    def __str__(self) -> str:
        return str(self.title)
    