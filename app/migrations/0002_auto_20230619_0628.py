# Generated by Django 3.2.19 on 2023-06-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Total_Seat',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='long_desc',
            field=models.TextField(default='', null=True),
        ),
    ]