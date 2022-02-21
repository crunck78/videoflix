from datetime import date
from pydoc import describe
from venv import create
from django.db import models

# Create your models here.
class Video(models.Model):
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    Video_file = models.FileField(upload_to='videos', blank=True, null=True)

    def __str__(self) -> str:
        return '[' + self.section.module.title + '] - ' + self.title
