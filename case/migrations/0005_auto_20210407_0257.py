# Generated by Django 3.1.7 on 2021-04-07 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0004_auto_20210406_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
