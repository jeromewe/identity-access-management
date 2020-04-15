#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: sun
@license: (C) Copyright 2016-2019, Light2Cloud (Beijing) Web Service Co., LTD
@contact: wenhaijie@light2cloud.com
@software: L2CloudCMP
@file: amazon_credential.py
@ide: PyCharm
@time: 2020/2/10 20:56
@desc:
"""
import uuid
from django.db import models
from organization.mixins.models import OrgModelMixin
from django.utils.translation import ugettext_lazy as _
# from django.core.validators import MinValueValidator, MaxValueValidator

from common import fields


__all__ = ['AmazonCredential', 'AmazonCredentialRole']


class BaseModel(OrgModelMixin):
    SOURCE = ''
    SOURCE_CHINA = 'amazon-china'
    SOURCE_STANDARD = 'amazon-standard'
    SOURCE_CHOICES = (
        (SOURCE_CHINA, 'Amazon China (Beijing, Ningxia)'),
        (SOURCE_STANDARD, 'Amazon Standard'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    credentials_name = models.CharField(
        max_length=256, verbose_name=_('Credentials Name')
    )
    account_type = models.CharField(
        max_length=30, choices=SOURCE_CHOICES, verbose_name="Account Type"
    )
    credential_type = models.CharField(
        max_length=128, verbose_name="Credentials Type"
    )
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Date created')
    )
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name=_("Date updated")
    )
    created_by = models.CharField(
        max_length=128, null=True, verbose_name=_('Created by')
    )

    class Meta:
        abstract = True


class AmazonCredential(BaseModel):
    user = models.ForeignKey(
        'account.User', on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_("User"), related_name="user_credential"
    )
    access_key_id = fields.EncryptCharField(
        max_length=256, verbose_name="Access Key ID"
    )
    secret_access_key = fields.EncryptCharField(
        max_length=256, verbose_name="Secret Access Key"
    )

    def __str__(self):
        return '{0.user}({0.credentials_name})'.format(self)

    def credentials_amount(self):
        amount = AmazonCredential.objects.filter(user=self.user)
        return amount.count()
        # if amount.count()

    class Meta:
        ordering = ['access_key_id']
        unique_together = [('user', 'access_key_id')]
        verbose_name = _("Amazon Credential")


class AmazonCredentialRole(BaseModel):
    user = models.ForeignKey(
        'account.User', on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_("User"), related_name="user_credential_role"
    )
    role_arn = fields.EncryptCharField(
        max_length=256, verbose_name="Amazon Credential Role Arn"
    )
    external_id = models.CharField(
        max_length=128, verbose_name="External ID", null=True, blank=True
    )
    require_mfa = models.BooleanField(
        default=False, blank=True, verbose_name="Require MFA"
    )
    is_local_role = models.BooleanField(
        default=False, blank=True,
        verbose_name="Whether to choose a local role"
    )

    def __str__(self):
        return '{0.user}({0.credentials_name})'.format(self)

    class Meta:
        ordering = ['role_arn']
        unique_together = [('user', 'role_arn')]
        verbose_name = _("Amazon Credential Role")
