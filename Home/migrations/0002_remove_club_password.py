# Generated by Django 5.0.1 on 2024-01-03 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='password',
        ),
    ]
