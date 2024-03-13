from django.urls import path
from .views import *

urlpatterns = [
    path("books-list/", BookList.as_view()),
    path("random-book/", RandomBook.as_view()),
    path("books-categories/", BooksCategoriesList.as_view()),
    path("book-by-category/<str:category>/", BooksByCategory.as_view()),
    path("book-by-name/<str:book_name>/", BooksByName.as_view()),
]
