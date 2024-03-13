from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, FSInputFile, Message
from keyboards.bot_kb import Keyboards  # pyright:ignore

import requests
import os

router = Router()
keyboards = Keyboards()


@router.message(Command("start"))
async def command_start(message: Message):
    await message.answer(
        "Hello! Thank you that you join us!",
        reply_markup=await keyboards.user_keyboard(),
    )


@router.message(Command("books_list"))
async def command_books_list(message: Message):
    response = requests.get("http://127.0.0.1:8000/api/books-list/")
    if response.status_code == 200:
        for book in response.json():
            print(book)
            await message.answer(book["name"])


@router.message(Command("random_book"))
async def command_random_book(message: Message):
    response = requests.get("http://127.0.0.1:8000/api/random-book/")
    if response.status_code == 200:
        book = response.json()[0]
        book_image = book["image"]
        file = FSInputFile(
            os.path.join(
                os.getcwd()[:-4], "admin_panel", "books_images", book_image[14:]
            ),
            filename=book_image[14:],
        )
        await message.answer_photo(
            photo=file, caption=f"Name:{book['name']}.Description:{book['description']}"
        )


@router.message(Command("books_by_category"))
async def command_books_by_category(message: Message):
    await message.answer(
        "Choose genre", reply_markup=await keyboards.books_by_category()
    )


@router.message(Command("books"))
async def command_books(message: Message):
    await message.answer("Choose book", reply_markup=await keyboards.books())


@router.callback_query(F.data.startswith("category_"))
async def get_book_by_category(callback_query: CallbackQuery):
    category_name = callback_query.data[9:]
    response = requests.get(
        f"http://127.0.0.1:8000/api/book-by-category/{category_name}"
    )
    if response.status_code == 200:
        books = response.json()
        for book in books:
            book_image = book["image"]
            file = FSInputFile(
                os.path.join(
                    os.getcwd()[:-4], "admin_panel", "books_images", book_image[14:]
                ),
                filename=book_image[14:],
            )
            await callback_query.message.answer_photo(
                photo=file,
                caption=f"Name:{book['name']}.Description:{book['description']}",
            )


@router.callback_query(F.data.startswith("book_"))
async def get_book_by_name(callback_query: CallbackQuery):
    book_name = callback_query.data[5:]
    response = requests.get(f"http://127.0.0.1:8000/api/book-by-name/{book_name}")
    if response.status_code == 200:
        book = response.json()[0]
        book_image = book["image"]
        file = FSInputFile(
            os.path.join(
                os.getcwd()[:-4], "admin_panel", "books_images", book_image[14:]
            ),
            filename=book_image[14:],
        )
        await callback_query.message.answer_photo(
            photo=file,
            caption=f"Name:{book['name']}.Description:{book['description']}",
        )
