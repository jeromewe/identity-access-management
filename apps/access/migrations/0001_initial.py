# Generated by Django 2.2.9 on 2020-02-14 12:59

import common.fields.model
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
            name='AmazonCredentialRole',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('credentials_name', models.CharField(max_length=256, verbose_name='Credentials Name')),
                ('account_type', models.CharField(choices=[('amazon-china', 'Amazon China (Beijing, Ningxia)'), ('amazon-standard', 'Amazon Standard')], max_length=30, verbose_name='Account Type')),
                ('credential_type', models.CharField(max_length=128, verbose_name='Credentials Type')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('created_by', models.CharField(max_length=128, null=True, verbose_name='Created by')),
                ('role_arn', common.fields.model.EncryptCharField(max_length=256, verbose_name='Amazon Credential Role Arn')),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, verbose_name='External ID')),
                ('require_mfa', models.BooleanField(blank=True, default=False, verbose_name='Require MFA')),
                ('is_local_role', models.BooleanField(blank=True, default=False, verbose_name='Whether to choose a local role')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_credential_role', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Amazon Credential Role',
                'ordering': ['role_arn'],
                'unique_together': {('user', 'role_arn')},
            },
        ),
        migrations.CreateModel(
            name='AmazonCredential',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('credentials_name', models.CharField(max_length=256, verbose_name='Credentials Name')),
                ('account_type', models.CharField(choices=[('amazon-china', 'Amazon China (Beijing, Ningxia)'), ('amazon-standard', 'Amazon Standard')], max_length=30, verbose_name='Account Type')),
                ('credential_type', models.CharField(max_length=128, verbose_name='Credentials Type')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('created_by', models.CharField(max_length=128, null=True, verbose_name='Created by')),
                ('access_key_id', common.fields.model.EncryptCharField(max_length=256, verbose_name='Access Key ID')),
                ('secret_access_key', common.fields.model.EncryptCharField(max_length=256, verbose_name='Secret Access Key')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_credential', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Amazon Credential',
                'ordering': ['access_key_id'],
                'unique_together': {('user', 'access_key_id')},
            },
        ),
    ]
