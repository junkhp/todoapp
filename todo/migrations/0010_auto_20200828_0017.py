# Generated by Django 2.2.15 on 2020-08-27 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20200828_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='duedate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='締め切り日'),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', '高い'), ('warning', '普通'), ('primary', '低い')], default='warning', max_length=50, verbose_name='優先度'),
        ),
    ]
