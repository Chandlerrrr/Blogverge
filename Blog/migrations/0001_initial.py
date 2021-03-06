# Generated by Django 3.1.2 on 2020-11-25 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('tags', models.CharField(default='AddTags', max_length=255)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('Adventure', 'Adventure'), ('Blog', 'Blog'), ('Photography', 'Photography'), ('Culture', 'Culture'), ('Tv', 'Tv'), ('Fashion', 'Fashion'), ('Lifestyle', 'Lifestyle'), ('Life', 'Life'), ('God', 'God'), ('Movies', 'Movies'), ('Culture', 'Culture'), ('Weather', 'Weather'), ('Art', 'Art'), ('Space', 'Space'), ('Nature', 'Nature'), ('Computer', 'Computer'), ('SocialMedia', 'SocialMedia')], default='AddCategory', max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Blog.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
