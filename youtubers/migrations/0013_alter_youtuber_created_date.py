# Generated by Django 4.1.1 on 2022-09-12 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0012_alter_youtuber_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 12, 18, 2, 26, 662416)),
        ),
    ]
