# Generated by Django 5.0.2 on 2024-03-01 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyPanel', '0009_alter_attendancerecord_upload_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='examid',
        ),
        migrations.AlterField(
            model_name='attendancerecord',
            name='upload_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 1, 9, 40, 55, 414290, tzinfo=datetime.timezone.utc)),
        ),
    ]