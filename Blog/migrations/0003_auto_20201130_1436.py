# Generated by Django 3.1.2 on 2020-11-30 09:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20201130_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 9, 6, 35, 851941, tzinfo=utc)),
        ),
    ]
