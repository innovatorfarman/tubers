# Generated by Django 4.1.1 on 2022-09-12 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_register_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
    ]