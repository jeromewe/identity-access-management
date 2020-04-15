#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: sun
@license: (C) Copyright 2016-2019, Light2Cloud (Beijing) Web Service Co., LTD
@contact: wenhaijie@light2cloud.com
@software: L2CloudCMP
@file: access_key.py
@ide: PyCharm
@time: 2019/12/20 12:13
@desc:
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework_bulk import BulkModelViewSet
from rest_framework.serializers import ValidationError
from organization.mixins import generics
from common.permissions import IsValidUser, IsOrgAdminOrAppUser
from .. import serializers
from ..models import AccessKey
__all__ = [
    'AccessKeyViewSet', 'AccessKeyListView'
]


class AccessKeyViewSet(BulkModelViewSet):
    permission_classes = (IsValidUser,)
    serializer_class = serializers.AccessKeySerializer
    search_fields = ["^access_key_id", "is_active", "date_created"]

    def get_queryset(self):
        return self.request.user.access_keys.all()

    def create(self, request, *args, **kwargs):
        user = self.request.user
        access_key = user.create_access_key()
        if user.access_keys.all().count() > 3:
            raise ValidationError(
                {
                    'code': 400, 'error_code': '40002',
                    'msg': '访问密钥已达上限，无法生成新的访问密钥'
                }
            )
        else:
            return Response(
                {
                    'code': 201,
                    'data': {
                        'access_key_id': access_key.access_key_id,
                        'secret_access_key': access_key.secret_access_key
                    },
                    'msg': '这是仅有的一次查看或下载私有访问密钥的机会。以后您无法恢复它们。不过，您随时可以创建新的访问密钥'
                },
                status=status.HTTP_201_CREATED
            )


class AccessKeyListView(generics.ListAPIView):

    serializer_class = serializers.AccessKeySerializer
    permission_classes = [IsOrgAdminOrAppUser]
    http_method_names = ['get']
    filter_fields = [
        "id", "user", "access_key_id", "is_active", "date_created"
    ]
    search_fields = filter_fields

    def get_object(self):
        pk = self.kwargs.get('pk')
        return AccessKey.objects.filter(user=pk)

    def get_queryset(self):
        queryset = self.get_object()
        return queryset
