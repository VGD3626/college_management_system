# Generated by Django 5.0.2 on 2024-03-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acPanel', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='verification_status',
            field=models.BooleanField(default=False),
        ),
    ]
