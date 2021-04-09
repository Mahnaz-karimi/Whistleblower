# Generated by Django 3.1.7 on 2021-04-07 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0009_auto_20210407_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('Ny', 'Sagen er nyoprettet'), ('Behandles', 'Sagen behandles'), ('Lukket', 'Sagen er lukket'), ('Afvist', 'Sagen er afvist')], default='Ny', max_length=32),
        ),
    ]
