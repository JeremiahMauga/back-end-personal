# Generated by Django 3.2.6 on 2021-08-13 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210812_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='gems',
            field=models.IntegerField(verbose_name=10),
        ),
    ]