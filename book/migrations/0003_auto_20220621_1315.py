# Generated by Django 3.1.5 on 2022-06-21 13:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20220621_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 13, 15, 56, 171755, tzinfo=utc)),
        ),
    ]
