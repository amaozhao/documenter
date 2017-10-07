from __future__ import unicode_literals

from django.contrib import admin
from document.models import Topic, Project, Chapter


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Chapter)
class ChaperAdmin(admin.ModelAdmin):
    pass
