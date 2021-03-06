# Generated by Django 3.1.2 on 2020-12-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_auto_20201202_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='upload_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(auto_now_add=True),
        ),
    ]
