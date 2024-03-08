from django.urls import path
from .views import BookList, RandomBook

urlpatterns = [
    path("books-list/", BookList.as_view()),
    path("random-book/", RandomBook.as_view()),
]
