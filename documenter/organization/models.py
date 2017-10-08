from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Organization(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=100,
        unique=True,
    )
    description = models.TextField(verbose_name=_('description'))
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('author'),
        related_name='organizations'
    )
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
        db_table = 'organization'
        verbose_name = _('organization')
        verbose_name_plural = _('organizations')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class OrganizationUser(models.Model):
    organization = models.ForeignKey(
        Organization,
        verbose_name=_('organization'),
        on_delete=models.CASCADE,
        related_name='organizations'
    )

    class Meta:
        db_table = 'role'
        verbose_name = _('role')
        verbose_name_plural = _('roles')

    def __str__(self):
        return self.name
