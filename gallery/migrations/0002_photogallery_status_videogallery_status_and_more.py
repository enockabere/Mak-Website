# Generated by Django 4.1 on 2022-08-05 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photogallery',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0, help_text='Change to Publish for it to be seen'),
        ),
        migrations.AddField(
            model_name='videogallery',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0, help_text='Change to Publish for it to be seen'),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='videogallery',
            name='video',
            field=models.FileField(upload_to='media'),
        ),
    ]
