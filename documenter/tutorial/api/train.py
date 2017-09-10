# coding: utf-8

from rest_framework import generics
from tutorial.models import Train
from tutorial.serializers import (
    # SimpleTrainSerializer,
    TrainSerializer
)


class TrainListView(generics.ListAPIView):
    model = Train
    serializer_class = TrainSerializer

    def get_queryset(self):
        chapter = self.kwargs.get('chapter')
        query = self.model.objects.select_related(
            'author', 'chapter').filter(chapter=chapter)
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(title__contains=title)
        return query.order_by('id')


class TrainDetailView(generics.RetrieveAPIView):
    model = Train
    serializer_class = TrainSerializer

    def get_queryset(self):
        query = self.model.objects.select_related(
            'author', 'chapter')
        return query
