# Generated by Django 4.0 on 2022-01-05 01:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_schedule', '0002_schedule_date_alter_schedule_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
    ]
