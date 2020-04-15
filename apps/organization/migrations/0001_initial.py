# Generated by Django 2.2.9 on 2020-02-02 08:03

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('comment', models.TextField(blank=True, default='', max_length=128, verbose_name='Comment')),
                ('admins', models.ManyToManyField(blank=True, related_name='related_admin_orgs', to=settings.AUTH_USER_MODEL)),
                ('auditors', models.ManyToManyField(blank=True, related_name='related_audit_orgs', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(blank=True, related_name='related_user_orgs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Organization',
            },
        ),
    ]