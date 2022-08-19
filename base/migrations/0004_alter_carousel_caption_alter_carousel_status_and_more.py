# Generated by Django 4.1 on 2022-08-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_calltoactionpanel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='caption',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0, help_text='Change to Published for it to be seen'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='title',
            field=models.CharField(blank=True, default='Our Sand, Our livelihood', max_length=100),
        ),
    ]
