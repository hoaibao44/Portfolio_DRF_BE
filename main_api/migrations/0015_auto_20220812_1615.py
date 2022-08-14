# Generated by Django 3.1.1 on 2022-08-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0014_auto_20220812_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='whoami',
            name='hobbies',
        ),
        migrations.AddField(
            model_name='whoami',
            name='hobbies',
            field=models.ManyToManyField(blank=True, related_name='hobbies', to='main_api.Hobbies'),
        ),
    ]
