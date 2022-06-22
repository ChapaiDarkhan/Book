from django.utils import timezone
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=121)
    publisher = models.CharField(max_length=121)
    author = models.CharField(max_length=121)
    pages = models.PositiveIntegerField()
    tags = models.CharField(max_length=226)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
