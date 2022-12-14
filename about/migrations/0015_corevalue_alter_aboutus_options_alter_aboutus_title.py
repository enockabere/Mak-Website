# Generated by Django 4.1 on 2022-09-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0014_alter_servicecharter_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Our Vision', max_length=200)),
                ('statement', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0, help_text='Change to Publish for it to be seen')),
            ],
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'Background Info', 'verbose_name_plural': 'Background Info'},
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.CharField(default='Background Infomation', max_length=200),
        ),
    ]
