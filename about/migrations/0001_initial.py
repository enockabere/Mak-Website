# Generated by Django 4.0.6 on 2022-08-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MDsMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text="e.g. John's Message", max_length=200)),
                ('message', models.TextField()),
                ('signature', models.ImageField(upload_to='')),
                ('name_of_md', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=50)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0, help_text='Change to Publish for it to be seen')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('statement', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, help_text='Optional', max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, help_text='Image size should be in .jpg or .png', null=True, upload_to='media')),
                ('category', models.IntegerField(choices=[(0, 'Board of management'), (1, 'Management')], default=0, help_text='select Peronel membership title')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0, help_text='Change to Publish for it to be seen')),
            ],
        ),
    ]
