# Generated by Django 4.0.6 on 2022-07-29 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_alter_notifications_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='category',
            field=models.CharField(choices=[('Electrical', 'Electrical'), ('Mechanical', 'Mechanical')], max_length=10),
        ),
    ]