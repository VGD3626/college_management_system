# Generated by Django 5.0.2 on 2024-03-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acPanel', '0004_remove_accountant_person_remove_accountant_userid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='bank',
            field=models.CharField(default='bank of baroda', max_length=40),
            preserve_default=False,
        ),
    ]
