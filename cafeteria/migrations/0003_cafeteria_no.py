# Generated by Django 3.1.2 on 2024-05-31 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0002_auto_20240531_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafeteria',
            name='No',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]