# Generated by Django 3.1.1 on 2022-08-04 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='whoami',
            name='birth_day',
            field=models.DateField(),
        ),
    ]
