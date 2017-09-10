# coding: utf-8

from rest_framework import generics
from tutorial.models import Chapter
from tutorial.serializers import (
    SimpleChaperSerializer,
    ChaperSerializer
)


class ChapterListView(generics.ListAPIView):
    model = Chapter
    serializer_class = SimpleChaperSerializer

    def get_queryset(self):
        tutorial = self.kwargs.get('tutorial')
        query = self.model.objects.filter(tutorial=tutorial)
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(title__contains=title)
        return query.order_by('id')


class ChapterDetailView(generics.RetrieveAPIView):
    model = Chapter
    serializer_class = ChaperSerializer

    def get_queryset(self):
        query = self.model.objects.select_related('author', 'tutorial')
        return query
