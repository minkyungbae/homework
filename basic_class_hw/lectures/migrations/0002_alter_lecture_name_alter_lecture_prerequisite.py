# Generated by Django 4.2 on 2025-01-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='prerequisite',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
