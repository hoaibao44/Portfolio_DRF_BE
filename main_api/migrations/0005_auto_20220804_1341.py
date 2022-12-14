# Generated by Django 3.1.1 on 2022-08-04 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0004_auto_20220804_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='take_away',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='whoami',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]
