# Generated by Django 3.1.5 on 2022-06-21 11:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 11, 4, 31, 820775, tzinfo=utc)),
        ),
    ]