# Generated by Django 3.0.2 on 2020-02-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_auto_20200218_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='priority',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lists',
            name='task',
            field=models.CharField(max_length=2000),
        ),
    ]
