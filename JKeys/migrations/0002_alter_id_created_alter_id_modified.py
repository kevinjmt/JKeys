# Generated by Django 4.1.5 on 2023-02-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JKeys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='id',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
