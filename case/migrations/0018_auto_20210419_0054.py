# Generated by Django 3.1.7 on 2021-04-19 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caseworker', '0002_auto_20210416_0026'),
        ('case', '0017_auto_20210419_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caseinfo',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='caseworker.company'),
        ),
    ]
