# Generated by Django 3.0.2 on 2020-02-18 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='list',
            name='task',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]