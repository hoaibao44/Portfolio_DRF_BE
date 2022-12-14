# Generated by Django 3.1.1 on 2022-08-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0007_auto_20220804_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name': 'Org',
                'verbose_name_plural': 'Orgs',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='org',
            field=models.ManyToManyField(blank=True, null=True, related_name='org', to='main_api.Org'),
        ),
    ]
