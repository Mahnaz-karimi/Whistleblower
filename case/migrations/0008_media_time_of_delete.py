# Generated by Django 3.1.7 on 2021-04-07 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0007_auto_20210407_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='time_of_delete',
            field=models.DateField(blank=True, null=True),
        ),
    ]
