from django.db import models
from django.contrib.auth.models import User
from datetime import time


class Schedule(models.Model):
    user = models.ForeignKey(
        User, related_name="schedules", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    date = models.DateField(default="2022-01-03")
    time = models.TimeField(default=time(9, 00))

    def __str__(self):
        return f"{self.user} - {self.name} : {self.date} {self.time}"
