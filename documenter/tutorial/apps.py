# coding: utf-8

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TutorialConfig(AppConfig):
    name = 'tutorial'
    verbose_name = _('Tutorials')
