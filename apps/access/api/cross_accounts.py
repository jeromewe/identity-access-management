#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: sun
@license: (C) Copyright 2016-2019, Light2Cloud (Beijing) Web Service Co., LTD
@contact: wenhaijie@light2cloud.com
@software: L2CloudCMP
@file: cross_accounts.py
@ide: PyCharm
@time: 2020/2/15 10:39
@desc:
"""
from django.conf import settings
from django.core.cache import cache
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.permissions import IsValidUser
from common.utils import generate_random_string


class CrossAccountsListView(APIView):
    http_method_names = ['get']
    permission_classes = (IsValidUser,)
    object = None

    def get(self, request):
        user = self.request.user.email

        if settings.CHINA_REQUIRE_EXTERNAL_ID:
            china = 'china-' + user
            china_external_id = settings.CHINA_EXTERNAL_ID + generate_random_string(8)
            if cache.get(china, None) is None:
                cache.set(china, china_external_id, timeout=60 * 3)
                cache_china_external_id = cache.get(china, None)
            else:
                cache_china_external_id = cache.get(china, None)
        else:
            cache_china_external_id = ''

        if settings.GLOBAL_REQUIRE_EXTERNAL_ID:
            key = 'global-' + user
            global_external_id = settings.GLOBAL_EXTERNAL_ID + generate_random_string(8)
            if cache.get(key, None) is None:
                cache.set(key, global_external_id, timeout=60 * 3)
                cache_global_external_id = cache.get(key, None)
            else:
                cache_global_external_id = cache.get(key, None)
        else:
            cache_global_external_id = ''

        data = {
            "code": status.HTTP_200_OK,
            "data": [
                {
                    'region': 'Amazon China',
                    'AccountID': settings.CHINA_ACCOUNT_ID,
                    'RequireExternalID': settings.CHINA_REQUIRE_EXTERNAL_ID,
                    'ExternalID': cache_china_external_id,
                    'RequireMFA': settings.CHINA_REQUIRE_MFA,
                },
                {
                    'region': 'Amazon Global',
                    'AccountID': settings.GLOBAL_ACCOUNT_ID,
                    'RequireExternalID': settings.GLOBAL_REQUIRE_EXTERNAL_ID,
                    'ExternalID': cache_global_external_id,
                    'RequireMFA': settings.GLOBAL_REQUIRE_MFA,
                }
            ],
            "msg": "跨账户填入的账户信息"
        }
        return Response(data, status=status.HTTP_200_OK)
