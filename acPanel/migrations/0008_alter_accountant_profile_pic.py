# Generated by Django 5.0.2 on 2024-03-31 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acPanel', '0007_accountant_email_accountant_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountant',
            name='profile_pic',
            field=models.ImageField(default='default_profile.jpeg', upload_to='profile_pics'),
        ),
    ]