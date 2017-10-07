from __future__ import unicode_literals

import markdown
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


markdown_extensions = ['pymdownx.arithmatex', 'pymdownx.github']


@python_2_unicode_compatible
class Topic(MPTTModel):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=100,
        unique=True,
    )
    description = models.TextField(verbose_name=_('description'))
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('author'),
        related_name='topics'
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
        db_table = 'topic'
        verbose_name = _('topic')
        verbose_name_plural = _('topics')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Project(models.Model):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=100,
    )
    content = models.TextField(verbose_name=_('content'))
    is_private = models.BooleanField(
        verbose_name=_('is private'), default=False)
    topic = models.ForeignKey(
        Topic,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_('topic'),
        related_name='tutorials'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('author'),
        related_name='tutorials'
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
        db_table = 'project'
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        indexes = [
            models.Index(fields=['title'], name='idx_project_title'),
        ]

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Chapter(models.Model):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=100
    )
    content = models.TextField(verbose_name=_('content'))
    html = models.TextField(verbose_name=_('html'), editable=False)
    quote = models.TextField(verbose_name=_('quote'))
    is_private = models.BooleanField(
        verbose_name=_('is private'), default=False)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name=_('project'),
        related_name='chapters'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('author'),
        related_name='chapters'
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
        db_table = 'chapter'
        verbose_name = _('chapter')
        verbose_name_plural = _('chapters')
        indexes = [
            models.Index(fields=['title'], name='idx_chapter_title'),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        tutorial_private = self.tutorial.is_private
        if tutorial_private:
            self.is_private = True
        self.html = markdown.markdown(self.content, markdown_extensions, safe_mode='escape')
        super(Chapter, self).save(*args, **kwargs)
