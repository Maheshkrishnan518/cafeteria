# Generated by Django 3.1.2 on 2024-05-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafeteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('amount', models.IntegerField()),
                ('image_item', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cafeteria',
            },
        ),
    ]
