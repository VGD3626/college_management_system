# Generated by Django 5.0.2 on 2024-04-01 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managementPanel', '0002_remove_hod_person_remove_hod_userid_hod_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]
