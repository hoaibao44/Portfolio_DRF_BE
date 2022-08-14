# Generated by Django 3.1.1 on 2022-08-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0019_auto_20220813_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skill_type',
            field=models.TextField(choices=[('PER', 'personal'), ('PRO', 'professional')], default='PER', max_length=3),
        ),
    ]
