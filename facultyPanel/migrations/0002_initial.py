# Generated by Django 5.0.1 on 2024-02-27 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facultyPanel', '0001_initial'),
        ('studentPanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hallticket',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentPanel.student'),
        ),
        migrations.AddField(
            model_name='mark',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facultyPanel.exam'),
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentPanel.student'),
        ),
        migrations.AddField(
            model_name='hallticket',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facultyPanel.program'),
        ),
        migrations.AddField(
            model_name='exam',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facultyPanel.program'),
        ),
        migrations.AddField(
            model_name='subject',
            name='programe',
            field=models.ManyToManyField(to='facultyPanel.program'),
        ),
        migrations.AddField(
            model_name='mark',
            name='subject',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='facultyPanel.subject'),
        ),
    ]
