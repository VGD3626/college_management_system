# Generated by Django 5.0.2 on 2024-03-30 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acPanel', '0006_alter_payment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountant',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='accountant',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='accountant',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
