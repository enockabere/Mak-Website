# Generated by Django 4.1 on 2022-09-07 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0004_alter_jobadvert_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobadvert',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='deadline for application'),
        ),
        migrations.AddField(
            model_name='jobadvert',
            name='job_status',
            field=models.CharField(choices=[('open', 'open'), ('closed', 'closed')], default='open', max_length=20),
        ),
    ]