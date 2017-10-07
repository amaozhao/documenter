# coding: utf-8

from __future__ import unicode_literals

from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from document.api import (
    TopicViewSet,
    SimpleProjectListView, ProjectListView, ProjectDetailView,
    ChapterListView, ChapterDetailView,
)


router = DefaultRouter()
router.register(r'topics', TopicViewSet, base_name='topic')

urlpatterns = router.urls + [
    # tutorials 路由
    url(r'^projects/$', SimpleProjectListView.as_view()),
    url(r'^topic-projects/(?P<topic>[0-9]+)/$', ProjectListView.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', ProjectDetailView.as_view()),

    # chapters 路由
    url(r'^project-chapters/(?P<project>[0-9]+)/$', ChapterListView.as_view()),
    url(r'^chapters/(?P<pk>[0-9]+)/$', ChapterDetailView.as_view()),
]
