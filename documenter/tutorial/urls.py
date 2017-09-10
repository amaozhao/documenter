# coding: utf-8

from __future__ import unicode_literals

from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from tutorial.api import (
    TopicViewSet,
    SimpleTutorialListView, TutorialListView, TutorialDetailView,
    ChapterListView, ChapterDetailView,
    TrainListView, TrainDetailView,
    AnswerListView
)


router = DefaultRouter()
router.register(r'topics', TopicViewSet, base_name='topic')

urlpatterns = router.urls + [
    # tutorials 路由
    url(r'^tutorials/$', SimpleTutorialListView.as_view()),
    url(r'^topic-tutorials/(?P<topic>[0-9]+)/$', TutorialListView.as_view()),
    url(r'^tutorials/(?P<pk>[0-9]+)/$', TutorialDetailView.as_view()),

    # chapters 路由
    url(r'^tutorial-chapters/(?P<tutorial>[0-9]+)/$', ChapterListView.as_view()),
    url(r'^chapters/(?P<pk>[0-9]+)/$', ChapterDetailView.as_view()),

    # trains 路由
    url(r'^chapter-trains/(?P<chapter>[0-9]+)/$', TrainListView.as_view()),
    url(r'^trains/(?P<pk>[0-9]+)/$', TrainDetailView.as_view()),

    # answers 路由
    url(r'^train-answers/(?P<train>[0-9]+)/$', AnswerListView.as_view()),
]