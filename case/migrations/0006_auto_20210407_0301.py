# Generated by Django 3.1.7 on 2021-04-07 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0005_auto_20210407_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
