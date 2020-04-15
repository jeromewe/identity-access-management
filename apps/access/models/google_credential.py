#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: sun
@license: (C) Copyright 2016-2019, Light2Cloud (Beijing) Web Service Co., LTD
@contact: wenhaijie@light2cloud.com
@software: L2CloudCMP
@file: google_credential.py
@ide: PyCharm
@time: 2020/4/11 19:05
@desc:
"""
import uuid
from django.db import models
from django.contrib.postgres.fields import JSONField
from rest_framework.utils.encoders import JSONEncoder
from organization.mixins.models import OrgModelMixin
from django.utils.translation import ugettext_lazy as _

__all__ = ['GoogleCredential']


class GoogleCredential(OrgModelMixin):
    SOURCE = ''
    GOOGLE_STANDARD = 'google-standard'
    SOURCE_CHOICES = (
        (GOOGLE_STANDARD, 'Google Standard (Commercial)'),
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(
        'account.User', on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_("User"), related_name="user_credential"
    )
    credentials_name = models.CharField(
        max_length=256, verbose_name=_('Credentials Name')
    )
    google_service_account_key_json = JSONField(
        db_index=True, encoder=JSONEncoder,
        verbose_name=_("Google Service Account Key JSON")
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

    def __str__(self):
        return '{0.user}({0.credentials_name})'.format(self)

    class Meta:
        ordering = ['credentials_name']
        unique_together = [('user', 'google_service_account_key_json')]
        verbose_name = _("Google Credential")
