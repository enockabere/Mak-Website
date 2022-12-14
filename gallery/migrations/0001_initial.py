# Generated by Django 4.1 on 2022-08-11 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('caption', models.TextField(blank=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0, help_text='Change to Publish for it to be seen')),
            ],
            options={
                'verbose_name_plural': 'Photo Galleries',
            },
        ),
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='media')),
                ('caption', models.TextField(blank=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0, help_text='Change to Publish for it to be seen')),
            ],
            options={
                'verbose_name_plural': 'Video Galleries',
            },
        ),
    ]
