# Generated by Django 4.1 on 2024-05-18 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_folders_created_at_alter_folders_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='places',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
