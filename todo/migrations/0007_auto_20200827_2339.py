# Generated by Django 2.2.15 on 2020-08-27 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_howtoorder'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='howtoorder',
            table='how_to_order',
        ),
        migrations.AlterModelTable(
            name='todomodel',
            table='todo',
        ),
    ]
