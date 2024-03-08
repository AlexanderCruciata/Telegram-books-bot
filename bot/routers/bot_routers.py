from aiogram import Router
from aiogram.filters import Command
from aiogram.types import FSInputFile, InputFile, Message
from keyboards.bot_kb import Keyboards  # pyright:ignore
from create_bot import BOT_PATH  # pyright:ignore
import requests
import os

# дjбавить в модели джанго чтобы в image поле были абсолютные пути
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
            await message.answer(
                f"Name:{book['name']}.Description:{book['description']}"
            )


@router.message(Command("random_book"))
async def command_random_book(message: Message):
    response = requests.get("http://127.0.0.1:8000/api/random-book/")
    if response.status_code == 200:
        book = response.json()[0]
        image_path = os.path.join(BOT_PATH, book["image"])
        file_path = BOT_PATH[:-4] + book["image"]
        print(file_path)
        # дjбавить в модели джанго чтобы в image поле были абсолютные пути

        # await message.reply_photo(file)
