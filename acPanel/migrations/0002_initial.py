# Generated by Django 5.0.1 on 2024-02-27 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acPanel', '0001_initial'),
        ('studentPanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentPanel.student'),
        ),
    ]
