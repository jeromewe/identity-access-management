#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: sun
@license: (C) Copyright 2016-2019, Light2Cloud (Beijing) Web Service Co., LTD
@contact: wenhaijie@light2cloud.com
@software: L2CloudCMP
@file: tencent_credential.py
@ide: PyCharm
@time: 2020/4/11 19:06
@desc:
"""
import uuid
from django.db import models
from organization.mixins.models import OrgModelMixin
from django.utils.translation import ugettext_lazy as _

from common import fields

__all__ = [
    'TenCentCloudCredential'
]


class TenCentCloudCredential(OrgModelMixin):
    SOURCE = ''
    SOURCE_STANDARD = 'tencnt-standard'
    SOURCE_INTERNATIONAL = 'tencnt-international'
    SOURCE_CHOICES = (
        (SOURCE_STANDARD, '中国站'),
        (SOURCE_INTERNATIONAL, 'International'),
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
    user = models.ForeignKey(
        'account.User', on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_("User"), related_name="user_credential"
    )
    secret_id = fields.EncryptCharField(
        max_length=256, verbose_name="Secret ID"
    )
    secret_key = fields.EncryptCharField(
        max_length=256, verbose_name="Secret Key"
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

    def __str__(self):
        return '{0.user}({0.credentials_name})'.format(self)

    class Meta:
        ordering = ['secret_id']
        unique_together = [('user', 'secret_id')]
        verbose_name = _("Amazon Credential")
