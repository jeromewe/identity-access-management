#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: sun
@license: (C) Copyright 2016-2019, Light2Cloud (Beijing) Web Service Co., LTD
@contact: wenhaijie@light2cloud.com
@software: L2CloudCMP
@file: cerdential.py
@ide: PyCharm
@time: 2020/4/12 22:51
@desc:
"""
import uuid
from django.db import models
from organization.mixins.models import OrgModelMixin
from django.contrib.postgres.fields import JSONField
from rest_framework.utils.encoders import JSONEncoder
from django.utils.translation import ugettext_lazy as _
# from django.core.validators import MinValueValidator, MaxValueValidator

from common import fields


class Credentials(OrgModelMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    credentials_name = models.CharField(
        max_length=256, verbose_name=_('Credentials Name')
    )
    account_type = models.CharField(
        max_length=30, verbose_name="Account Type"
    )
    credential_type = models.CharField(
        max_length=128, verbose_name="Credentials Type"
    )
    user = models.ForeignKey(
        'account.User', on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_("User"), related_name="user_credential"
    )
    """AWS or AliYun or TenCnt AK/SK"""
    access_key_id = fields.EncryptCharField(
        max_length=256, blank=True, null=True,
        verbose_name="Access Key ID"
    )
    secret_access_key = fields.EncryptCharField(
        max_length=256, blank=True, null=True,
        verbose_name="Secret Access Key"
    )
    """AWS role"""
    role_arn = fields.EncryptCharField(
        max_length=256, blank=True, null=True,
        verbose_name="Amazon Credential Role Arn"
    )
    external_id = models.CharField(
        max_length=128, blank=True, null=True,
        verbose_name="External ID"
    )
    require_mfa = models.BooleanField(
        default=False, blank=True, verbose_name="Require MFA"
    )
    is_local_role = models.BooleanField(
        default=False, blank=True,
        verbose_name="Whether to choose a local role"
    )
    """Google"""
    google_service_account_key_json = JSONField(
        db_index=True, encoder=JSONEncoder,
        blank=True, null=True,
        verbose_name=_("Google Service Account Key JSON")
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
