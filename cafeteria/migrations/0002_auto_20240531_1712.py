# Generated by Django 3.1.2 on 2024-05-31 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafeteria',
            name='image_item',
            field=models.ImageField(upload_to='images'),
        ),
    ]
