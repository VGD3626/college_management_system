# Generated by Django 5.0.2 on 2024-03-10 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyPanel', '0016_alter_attendancerecord_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='upload_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 10, 17, 27, 43, 521874, tzinfo=datetime.timezone.utc)),
        ),
    ]