# Generated by Django 5.0.2 on 2024-03-04 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyPanel', '0012_remove_announcement_receiver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='upload_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 4, 9, 9, 44, 105372, tzinfo=datetime.timezone.utc)),
        ),
    ]
