# Generated by Django 3.2.19 on 2023-06-19 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230619_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='schedule_from',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='schedule_to',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
