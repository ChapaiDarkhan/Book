from book.views import BookView, BookDetailView
from django.urls import path

urlpatterns = [
    path("book/", BookView.as_view()),
    path("book/<int:pk>/", BookDetailView.as_view())
    ]
