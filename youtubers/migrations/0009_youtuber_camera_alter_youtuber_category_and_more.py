# Generated by Django 4.1.1 on 2022-09-10 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0008_alter_youtuber_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='camera',
            field=models.CharField(choices=[('canon', 'canon'), ('nikon', 'nikon'), ('panasonic', 'panasonic'), ('fuji', 'fuji')], default='NA', max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('Coding', 'coding'), ('Vlogs', 'vlogs'), ('Education', 'education'), ('Reviews', 'reviews')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 10, 16, 52, 16, 9526)),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=50),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='height',
            field=models.IntegerField(),
        ),
    ]