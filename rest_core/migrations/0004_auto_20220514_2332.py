# Generated by Django 3.2.13 on 2022-05-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_core', '0003_alter_task_taskid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AlterField(
            model_name='task',
            name='taskID',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]