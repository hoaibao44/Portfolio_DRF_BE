# Generated by Django 3.1.1 on 2022-08-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0016_whoami_profile_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='position',
            field=models.ManyToManyField(blank=True, related_name='pj_position', to='main_api.Position'),
        ),
    ]
