from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class BaseModel(models.Model):
    created = models.DateTimeField(
        verbose_name=_('created'),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name=_('updated'),
        auto_now=True
    )
    deleted = models.BooleanField(
        verbose_name=_('deleted'),
        default=False
    )

    class Meta:
        abstract = True
