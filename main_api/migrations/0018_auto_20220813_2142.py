# Generated by Django 3.1.1 on 2022-08-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0017_project_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]