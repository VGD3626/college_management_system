# Generated by Django 5.0.2 on 2024-03-01 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyPanel', '0007_attendancerecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='upload_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
