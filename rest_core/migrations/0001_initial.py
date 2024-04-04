# Generated by Django 3.2.13 on 2022-05-13 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rest_core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskID', models.IntegerField()),
                ('file', models.FileField(upload_to=rest_core.models.user_directory_path)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]