from django.contrib import admin
from .models import BookCategory, Book

admin.site.register(Book)
admin.site.register(BookCategory)
