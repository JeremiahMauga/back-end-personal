# Generated by Django 3.2.6 on 2021-08-14 23:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_inventory_gems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='gems',
        ),
        migrations.AddField(
            model_name='inventory',
            name='game_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]