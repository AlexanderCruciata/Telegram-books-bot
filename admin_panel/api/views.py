from rest_framework import generics
from rest_framework.mixins import Response
from rest_framework.views import APIView
from .models import BookCategory, Book
from .serializers import BookListSerializer, RandomBookSerializer
from random import uniform


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class RandomBook(APIView):
    def get(self, request):
        first_book_id = Book.objects.first().id
        last_book_id = Book.objects.last().id
        id_range = int(uniform(first_book_id, last_book_id))
        random_book = Book.objects.get(pk=id_range)
        serializer = RandomBookSerializer(random_book)
        return Response([serializer.data])
