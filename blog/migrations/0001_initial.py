# Generated by Django 3.2.7 on 2021-09-15 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('profile', models.ImageField(blank=True, default='default-thumnail.jpg', null=True, upload_to='')),
                ('bio', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('thumnail', models.ImageField(blank=True, default='default-thumnail.jpg', null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('author', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.userprofile')),
                ('categories', models.ManyToManyField(blank=True, to='blog.BlogCategory')),
            ],
        ),
    ]
