# coding: utf-8

from rest_framework import generics
from tutorial.models import Answer
from tutorial.serializers import (
    AnswerSerializer
)


class AnswerListView(generics.ListAPIView):
    model = Answer
    serializer_class = AnswerSerializer

    def get_queryset(self):
        train = self.kwargs.get('train')
        query = self.model.objects.select_related(
            'author', 'train').filter(train=train)
        return query.order_by('id')
