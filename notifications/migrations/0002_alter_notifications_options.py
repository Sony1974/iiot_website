# Generated by Django 4.0.6 on 2022-07-27 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notifications',
            options={'verbose_name': 'notification', 'verbose_name_plural': 'notifications'},
        ),
    ]