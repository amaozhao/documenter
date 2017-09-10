# coding: utf-8

from rest_framework import generics

from tutorial.models import Tutorial
from tutorial.serializers import TutorialSerializer, SimpleTutorialSerializer


class SimpleTutorialListView(generics.ListAPIView):
    model = Tutorial
    serializer_class = SimpleTutorialSerializer

    def get_queryset(self):
        query = self.model.objects
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(title__contains=title)
        return query.order_by('-updated')


class TutorialListView(generics.ListAPIView):
    model = Tutorial
    serializer_class = TutorialSerializer

    def get_queryset(self):
        topic = self.kwargs.get('topic')
        query = self.model.objects.filter(topic=topic)
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(title__contains=title)
        return query.all()


class TutorialDetailView(generics.RetrieveAPIView):
    model = Tutorial
    serializer_class = TutorialSerializer

    def get_queryset(self):
        return self.model.objects.select_related('author', 'topic')
