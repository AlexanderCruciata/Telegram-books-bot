from aiogram.types import pre_checkout_query
from rest_framework import generics
from rest_framework.mixins import Response
from rest_framework.views import APIView
from .models import BookCategory, Book, category_save
from .serializers import *
import random


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class RandomBook(APIView):
    def get(self, request):
        first_book_id = Book.objects.first().id
        last_book_id = Book.objects.last().id
        id_range = random.randint(first_book_id, last_book_id)
        random_book = Book.objects.get(pk=id_range)
        serializer = RandomBookSerializer(random_book)
        return Response([serializer.data])


class BooksCategoriesList(generics.ListAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BooksCategoriesSerializer


class BooksByCategory(APIView):
    def get(self, request, category):
        if category:
            category_object = BookCategory.objects.get(category_name=category)
            books = Book.objects.filter(category=category_object)
            serializer = BooksByCategorySerializer(books, many=True)
            return Response(serializer.data)


class BooksByName(APIView):
    def get(self, request, book_name):
        if book_name:
            book = Book.objects.get(name=book_name)
            serializer = BooksByCategorySerializer(book)
            return Response([serializer.data])
