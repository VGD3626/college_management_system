# Generated by Django 5.0.1 on 2024-02-17 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyPanel', '0001_initial'),
        ('userAuth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userAuth.person', to_field='user_id'),
        ),
    ]
