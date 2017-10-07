# coding: utf-8

from rest_framework import viewsets

from document.models import Topic
from document.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
