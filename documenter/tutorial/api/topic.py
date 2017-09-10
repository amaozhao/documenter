# coding: utf-8

from rest_framework import viewsets

from tutorial.models import Topic
from tutorial.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()