# Generated by Django 3.0.2 on 2020-03-01 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0005_tom'),
    ]

    operations = [
        migrations.CreateModel(
            name='List1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thing', models.CharField(max_length=2000)),
                ('allright', models.BooleanField(default=False)),
            ],
        ),
    ]