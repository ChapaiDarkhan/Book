from django.utils import timezone
from rest_framework import serializers
from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    created_at = serializers.DateTimeField(read_only=True, default=timezone.now)
    updated_at = serializers.DateTimeField(read_only=True, allow_null=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'publisher', 'author', 'pages', 'tags', 'created_at', 'updated_at')


class BookDetailSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True, default=timezone.now)

    class Meta:
        model = Book
        fields = ('id', 'title', 'publisher', 'author', 'pages', 'tags', 'created_at', 'updated_at')
