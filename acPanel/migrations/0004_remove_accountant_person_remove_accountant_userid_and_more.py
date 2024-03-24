# Generated by Django 5.0.2 on 2024-03-24 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acPanel', '0003_payment_verification_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountant',
            name='person',
        ),
        migrations.RemoveField(
            model_name='accountant',
            name='userId',
        ),
        migrations.AddField(
            model_name='accountant',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accountant',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='accountant',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='accountant',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='accountant',
            name='username',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
