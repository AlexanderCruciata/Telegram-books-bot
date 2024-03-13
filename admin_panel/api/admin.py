from django.contrib import admin
from .models import BookCategory, Book


class BookAdminModel(admin.ModelAdmin):
    list_display = ("name", "image")
    search_fields = ("name",)


class BookCategoryModel(admin.ModelAdmin):
    search_fields = ("category_name",)


admin.site.register(Book, BookAdminModel)
admin.site.register(BookCategory, BookCategoryModel)
