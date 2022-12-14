# Generated by Django 4.1.1 on 2022-09-10 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0005_alter_youtuber_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtuber',
            name='height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 10, 16, 32, 4, 193088)),
        ),
    ]
