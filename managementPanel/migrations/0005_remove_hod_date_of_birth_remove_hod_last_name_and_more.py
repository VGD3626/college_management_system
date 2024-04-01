# Generated by Django 5.0.2 on 2024-04-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementPanel', '0004_hod_date_of_birth_hod_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hod',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='hod',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='hod',
            name='middle_name',
        ),
        migrations.AlterField(
            model_name='hod',
            name='first_name',
            field=models.CharField(default='aaa', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hod',
            name='username',
            field=models.CharField(default='aaa', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventID', models.IntegerField()),
                ('eventname', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('starttime', models.DateField()),
                ('duration', models.DurationField()),
                ('hod', models.ManyToManyField(to='managementPanel.hod')),
            ],
        ),
    ]
