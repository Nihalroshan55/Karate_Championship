# Generated by Django 5.0.1 on 2024-01-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_candidate_entry_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='entry_fee',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]