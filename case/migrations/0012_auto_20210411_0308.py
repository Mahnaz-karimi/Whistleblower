# Generated by Django 3.1.7 on 2021-04-11 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0011_auto_20210407_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='case',
        ),
        migrations.RemoveField(
            model_name='media',
            name='images',
        ),
        migrations.AddField(
            model_name='media',
            name='case_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='caseinfo', to='case.caseinfo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='case',
            name='case_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_info', to='case.caseinfo'),
        ),
    ]
