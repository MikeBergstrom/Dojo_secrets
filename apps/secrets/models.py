# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime


class Secret(models.Model):
    secret = models.CharField(max_length=500)
    user = models.ForeignKey('login.User')
    like = models.ManyToManyField('login.User', related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Like(models.Model):
#     secret = models.ForeignKey(Secret, related_name="likes")
#     user = models.ForeignKey('login.User')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
