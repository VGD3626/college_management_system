# Generated by Django 5.0.2 on 2024-03-24 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acPanel', '0004_remove_accountant_person_remove_accountant_userid_and_more'),
        ('managementPanel', '0002_remove_hod_person_remove_hod_userid_hod_first_name_and_more'),
        ('userAuth', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]