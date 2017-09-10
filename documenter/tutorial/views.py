# coding: utf-8

from __future__ import unicode_literals

from rest_framework import viewsets, generics
from tutorial.models import Topic, Tutorial, Train, Answer
from tutorial.serializers import (
    TopicSerializer, TutorialSerializer, TrainSerializer, AnswerSerializer
)


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class TutorialViewSet(viewsets.ModelViewSet):
    model = Tutorial
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.all()

    def get_queryset(self):
        query = self.model.objects
        topic = self.request.GET.get('topic', None)
        if topic:
            query = query.filter(topic=topic)
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(title__contains=title)
        return query.all()


class TutorialListView(generics.ListCreateAPIView):
    model = Tutorial
    serializer_class = TutorialSerializer

    def get_queryset(self):
        query = self.model.objects
        topic = self.kwargs.get('topic')
        return query.filter(topic=topic).all()


class TrainViewSet(viewsets.ModelViewSet):
    model = Train
    serializer_class = TrainSerializer
    queryset = Train.objects.all()

    def get_queryset(self):
        query = self.model.objects
        tutorial = self.request.GET.get('tutorial', None)
        if tutorial:
            query = query.filter(tutorial=tutorial)
        content = self.request.GET.get('content', None)
        if content:
            query = query.filter(content__contains=content)
        return query.all()


class TrainListView(generics.ListCreateAPIView):
    model = Train
    serializer_class = TrainSerializer

    def get_queryset(self):
        query = self.model.objects
        tutorial = self.kwargs.get('tutorial')
        return query.filter(tutorial=tutorial).all()


class AnswerViewSet(viewsets.ModelViewSet):
    model = Answer
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get_queryset(self):
        query = self.model.objects
        tutorial = self.request.GET.get('tutorial', None)
        if tutorial:
            query = query.filter(tutorial=tutorial)
        content = self.request.GET.get('content', None)
        if content:
            query = query.filter(content__contains=content)
        return query.all()


class AnswerListView(generics.ListCreateAPIView):
    model = Answer
    serializer_class = AnswerSerializer

    def get_queryset(self):
        query = self.model.objects
        train = self.kwargs.get('train')
        return query.filter(train=train).all()
