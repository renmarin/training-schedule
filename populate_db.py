# some data for testing and presentation purposes

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'sport.settings')

import django
django.setup()

from training_schedule.models import Schedule, User
from random import choice
from datetime import time


users = {f'user-{num}': f'user-{num}-password' for num in range(10)}
trainings = ["Treadmill training ", "Leg presses", "Pull-ups", "Planks", "Swimming", "Weight training"]
dates = ["2022-01-06", "2022-01-07", "2022-01-08", "2022-01-09", "2022-01-10", "2022-01-11"]
times = [time(9, 00), time(12, 00), time(14, 00), time(16, 00), time(18, 00), time(20, 00)]

for username, password in users.items():
    user = User(
        username=username,
        password=password,
    )
    user.save()
    for _ in range(3):
        training = Schedule(
            user=user,
            name=choice(trainings),
            date=choice(dates),
            time=choice(times)
        )
        training.save()
