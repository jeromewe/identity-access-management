#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: sun
@license: (C) Copyright 2016-2019, Light2Cloud (Beijing) Web Service Co., LTD
@contact: wenhaijie@light2cloud.com
@software: L2CloudCMP
@file: backends.py
@ide: PyCharm
@time: 2019/12/19 16:35
@desc:
"""
from django.contrib.auth import get_user_model
from common.utils import get_logger
from .utils import new_client
from .models import OIDT_ACCESS_TOKEN

UserModel = get_user_model()

logger = get_logger(__file__)
client = new_client()


__all__ = [
    'OpenIDAuthorizationCodeBackend', 'OpenIDAuthorizationPasswordBackend',
]


class BaseOpenIDAuthorizationBackend(object):
    @staticmethod
    def user_can_authenticate(user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_valid = getattr(user, 'is_valid', None)
        return is_valid or is_valid is None

    def get_user(self, user_id):
        try:
            user = UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None


class OpenIDAuthorizationCodeBackend(BaseOpenIDAuthorizationBackend):
    def authenticate(self, request, **kwargs):
        logger.info('Authentication OpenID code backend')
        code = kwargs.get('code')
        redirect_uri = kwargs.get('redirect_uri')
        if not code or not redirect_uri:
            logger.info('Authenticate failed: No code or No redirect uri')
            return None
        try:
            oidt_profile = client.update_or_create_from_code(
                code=code, redirect_uri=redirect_uri
            )
        except Exception as e:
            logger.info('Authenticate failed: get oidt_profile: {}'.format(e))
            return None
        else:
            # Check openid user single logout or not with access_token
            request.session[OIDT_ACCESS_TOKEN] = oidt_profile.access_token
            user = oidt_profile.user
            logger.info('Authenticate success: user -> {}'.format(user))
            return user if self.user_can_authenticate(user) else None


class OpenIDAuthorizationPasswordBackend(BaseOpenIDAuthorizationBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        logger.info('Authentication OpenID password backend')
        if not username:
            logger.info('Authenticate failed: Not username')
            return None
        try:
            oidt_profile = client.update_or_create_from_password(
                username=username, password=password
            )
        except Exception as e:
            logger.error(e, exc_info=True)
            logger.info('Authenticate failed: get oidt_profile: {}'.format(e))
            return None
        else:
            user = oidt_profile.user
            logger.info('Authenticate success: user -> {}'.format(user))
            return user if self.user_can_authenticate(user) else None
