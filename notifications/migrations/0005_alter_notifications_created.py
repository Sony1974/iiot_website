# Generated by Django 4.0.6 on 2022-07-31 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_alter_notifications_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]