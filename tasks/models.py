from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=50, null=False)
    done        = models.BooleanField()
    created_at  = models.DateField()

    def __str__(self) -> str:
        return self.title