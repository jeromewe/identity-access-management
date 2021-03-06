#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: sun
@license: (C) Copyright 2016-2019, Light2Cloud (Beijing) Web Service Co., LTD
@contact: wenhaijie@light2cloud.com
@software: L2CloudCMP
@file: group.py
@ide: PyCharm
@time: 2019/12/19 15:52
@desc:
"""
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from organization.mixins.models import OrgModelMixin

__all__ = ['UserGroup']


class UserGroup(OrgModelMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    comment = models.TextField(blank=True, verbose_name=_('Comment'))
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_('Date created'))
    created_by = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def users_display(self):
        return ' '.join([user.username for user in self.users.all()])

    class Meta:
        ordering = ['name']
        unique_together = [('org_id', 'name'), ]
        verbose_name = _("User group")

    @classmethod
    def initial(cls):
        default_group = cls.objects.filter(name='Default')
        if not default_group:
            group = cls(name='Default', created_by='System', comment='Default user group')
            group.save()
        else:
            group = default_group[0]
        return group
