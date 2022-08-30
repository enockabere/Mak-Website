# Generated by Django 4.1 on 2022-08-30 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_alter_publication_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resources.pubcategory'),
        ),
    ]
