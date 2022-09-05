# Generated by Django 4.1 on 2022-08-29 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_alter_privacy_options_alter_publication_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.IntegerField(choices=[(0, 'Acts'), (1, 'Sand Dealers'), (2, 'Sand Harvesting Sites'), (3, 'Financial Reports'), (4, 'Application Form'), (5, 'Feedback Form')], default=0),
        ),
    ]