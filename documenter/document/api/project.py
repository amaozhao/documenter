# coding: utf-8

from rest_framework import generics

from document.models import Project
from document.serializers import ProjectSerializer, SimpleProjectSerializer


class SimpleProjectListView(generics.ListAPIView):
    model = Project
    serializer_class = SimpleProjectSerializer

    def get_queryset(self):
        query = self.model.objects
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(title__contains=title)
        return query.order_by('-updated')


class ProjectListView(generics.ListAPIView):
    model = Project
    serializer_class = Project

    def get_queryset(self):
        topic = self.kwargs.get('topic')
        query = self.model.objects.filter(topic=topic)
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(title__contains=title)
        return query.all()


class ProjectDetailView(generics.RetrieveAPIView):
    model = Project
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.model.objects.select_related('author', 'topic')
