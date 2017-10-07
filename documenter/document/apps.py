# coding: utf-8

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DocumentConfig(AppConfig):
    name = 'document'
    verbose_name = _('Document')
