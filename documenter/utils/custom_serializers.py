# coding: utf-8

from __future__ import unicode_literals

from rest_framework import serializers
from django.utils import timezone


class DateTimeField(serializers.DateTimeField):

    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeField, self).to_representation(value)


class DateField(serializers.DateField):

    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateField, self).to_representation(value)


class TimeField(serializers.TimeField):

    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(TimeField, self).to_representation(value)
