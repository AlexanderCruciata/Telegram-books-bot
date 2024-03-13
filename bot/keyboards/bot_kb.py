from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
import requests


class Keyboards:
    @staticmethod
    async def user_keyboard():
        builder = ReplyKeyboardBuilder()
        builder.button(text="/random_book")
        builder.button(text="/books_by_category")
        builder.button(text="/books")
        builder.adjust(1)
        return builder.as_markup()

    @staticmethod
    async def books_by_category():
        response = requests.get("http://127.0.0.1:8000/api/books-categories/")
        builder = InlineKeyboardBuilder()
        if response.status_code == 200:
            response = response.json()
            for category in response:
                category_name = category["category_name"]
                builder.button(
                    text=category_name, callback_data=f"category_{category_name}"
                )
        builder.adjust(2)
        return builder.as_markup()

    @staticmethod
    async def books():
        response = requests.get("http://127.0.0.1:8000/api/books-list/")
        builder = InlineKeyboardBuilder()
        if response.status_code == 200:
            response = response.json()
            for book in response:
                book_name = book["name"]
                builder.button(text=book_name, callback_data=f"book_{book_name}")
        builder.adjust(1)
        return builder.as_markup()
