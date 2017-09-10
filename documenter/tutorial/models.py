from __future__ import unicode_literals

import markdown
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from utils.base_models import BaseModel


markdown_extensions = ['pymdownx.arithmatex', 'pymdownx.github']


@python_2_unicode_compatible
class Topic(BaseModel, MPTTModel):
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

    class Meta:
        db_table = 'topic'
        verbose_name = _('topic')
        verbose_name_plural = _('topics')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Tutorial(BaseModel):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=100,
    )
    content = models.TextField(verbose_name=_('content'))
    is_private = models.BooleanField(
        verbose_name=_('is private'), default=False)
    topic = models.ForeignKey(
        Topic,
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

    class Meta:
        db_table = 'tutorial'
        verbose_name = _('tutorial')
        verbose_name_plural = _('tutorials')
        indexes = [
            models.Index(fields=['title'], name='idx_title'),
        ]

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Chapter(BaseModel):

    title = models.CharField(
        verbose_name=_('title'),
        max_length=100,
        db_index=True
    )
    content = models.TextField(verbose_name=_('content'))
    html = models.TextField(verbose_name=_('html'), editable=False)
    quote = models.TextField(verbose_name=_('quote'))
    is_private = models.BooleanField(
        verbose_name=_('is private'), default=False)
    tutorial = models.ForeignKey(
        Tutorial,
        on_delete=models.CASCADE,
        verbose_name=_('tutorial'),
        related_name='chapters'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('author'),
        related_name='chapters'
    )

    class Meta:
        db_table = 'chapter'
        verbose_name = _('chapter')
        verbose_name_plural = _('chapters')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        tutorial_private = self.tutorial.is_private
        if tutorial_private:
            self.is_private = True
        self.html = markdown.markdown(self.content, markdown_extensions)
        super(Chapter, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Train(BaseModel):
    content = models.TextField(_('content'), db_index=True)
    answer = models.TextField(_('answer'))
    html = models.TextField(verbose_name=_('html'), editable=False)
    is_private = models.BooleanField(
        verbose_name=_('is private'), default=False)
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        verbose_name=_('chapter'),
        related_name='trains'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('author'),
        related_name='trains'
    )

    class Meta:
        db_table = 'train'
        verbose_name = _('train')
        verbose_name_plural = _('trains')

    def __str__(self):
        if len(self.content) > 10:
            return self.content[:10] + '...'
        return self.content

    def save(self, *args, **kwargs):
        chapter_private = self.chapter.is_private
        if chapter_private:
            self.is_private = True
        self.html = markdown.markdown(self.content, markdown_extensions)
        super(Train, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Answer(BaseModel):
    content = models.TextField(_('content'), db_index=True)
    html = models.TextField(verbose_name=_('html'), editable=False)
    is_private = models.BooleanField(
        verbose_name=_('is private'), default=False)
    train = models.ForeignKey(
        Train,
        on_delete=models.CASCADE,
        verbose_name=_('train'),
        related_name='answers'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('author'),
        related_name='answers'
    )

    class Meta:
        db_table = 'answer'
        verbose_name = _('answer')
        verbose_name_plural = _('answers')

    def __str__(self):
        if len(self.content) > 10:
            return self.content[:10] + '...'
        return self.content

    def save(self, *args, **kwargs):
        train_private = self.train.is_private
        if train_private:
            self.is_private = True
        self.html = markdown.markdown(self.content, markdown_extensions)
        super(Answer, self).save(*args, **kwargs)

