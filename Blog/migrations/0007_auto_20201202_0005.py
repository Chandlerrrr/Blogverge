# Generated by Django 3.1.2 on 2020-12-01 18:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20201201_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 18, 35, 10, 260509, tzinfo=utc)),
        ),
    ]
