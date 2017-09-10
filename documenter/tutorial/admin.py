from __future__ import unicode_literals

from django.contrib import admin
from tutorial.models import Topic, Tutorial, Chapter, Train, Answer


class TopicAdmin(admin.ModelAdmin):
    pass


class TutorialAdmin(admin.ModelAdmin):
    pass


class TrainAdmin(admin.ModelAdmin):
    pass


class ChapterAdmin(admin.ModelAdmin):
    pass


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Topic, TopicAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Train, TrainAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Answer, AnswerAdmin)
