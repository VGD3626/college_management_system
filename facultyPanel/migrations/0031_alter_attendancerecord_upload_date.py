# Generated by Django 5.0.2 on 2024-04-01 04:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyPanel', '0030_alter_attendancerecord_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='upload_date',
            field=models.DateField(default=datetime.datetime(2024, 4, 1, 4, 11, 11, 820586, tzinfo=datetime.timezone.utc)),
        ),
    ]
