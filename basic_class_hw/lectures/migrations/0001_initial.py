# Generated by Django 4.2 on 2025-01-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lecture_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('instructor_id', models.IntegerField()),
                ('is_online', models.BooleanField()),
                ('prerequisite', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
