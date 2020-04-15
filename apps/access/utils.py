#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: sun
@license: (C) Copyright 2016-2019, Light2Cloud (Beijing) Web Service Co., LTD
@contact: wenhaijie@light2cloud.com
@software: L2CloudCMP
@file: utils.py
@ide: PyCharm
@time: 2020/2/14 16:05
@desc:
"""
from django.conf import settings
from access.models import AmazonCredential, AmazonCredentialRole

from common.utils import get_logger


logger = get_logger(__file__)


def credentials_amount(user):
    count = AmazonCredential.objects.filter(user=user).count() + AmazonCredentialRole.objects.filter(user=user).count()
    if count < settings.CREDENTIALS_MOST:
        return False
    return True
