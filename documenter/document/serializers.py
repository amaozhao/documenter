from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.utils.text import Truncator
from document.models import Topic, Project, Chapter
from rest_framework import serializers
from utils.custom_serializers import DateTimeField


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)


class SimpleTopicSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    created = DateTimeField()
    updated = DateTimeField()

    class Meta:
        model = Topic
        fields = (
            'id', 'title', 'description',
            'author', 'created', 'updated'
        )


class TopicSerializer(SimpleTopicSerializer):

    class Meta:
        model = Topic
        fields = (
            'id', 'title', 'description',
            'author', 'created', 'updated'
        )

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['author'] = user
        return super(TopicSerializer, self).create(validated_data)


class SimpleProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'title', 'content')


class ProjectSerializer(SimpleProjectSerializer):
    topic = SimpleTopicSerializer(read_only=True)
    author = UserSerializer(read_only=True)
    created = DateTimeField()
    updated = DateTimeField()

    class Meta:
        model = Project
        fields = (
            'id', 'title', 'content',
            'topic',
            'author',
            'created', 'updated'
        )


class SimpleChaperSerializer(serializers.ModelSerializer):
    tutorial = SimpleProjectSerializer(read_only=True)
    author = UserSerializer(read_only=True)
    created = DateTimeField()
    updated = DateTimeField()
    short_html = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = (
            'id', 'title', 'quote',
            'short_html', 'is_private',
            'tutorial', 'author', 'created', 'updated'
        )

    def get_short_html(self, obj):
        return Truncator(obj.html).chars(30, html=True)


class ChaperSerializer(SimpleChaperSerializer):

    class Meta:
        model = Chapter
        fields = (
            'id', 'title', 'quote',
            'html', 'is_private',
            'tutorial', 'author', 'created', 'updated'
        )
