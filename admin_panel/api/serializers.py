from rest_framework import serializers
from .models import Book, BookCategory


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book()
        fields = ("name",)


class RandomBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book()
        fields = ("name", "description", "image")


class BooksCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory()
        fields = ("category_name",)


class BooksByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book()
        fields = ("name", "description", "image")


class BooksByNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book()
        fields = "__all__"
