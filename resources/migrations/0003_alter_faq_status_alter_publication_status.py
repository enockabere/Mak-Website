# Generated by Django 4.1 on 2022-08-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_delete_jobadvert_delete_tender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0, help_text='Change to Publish for it to be seen'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
