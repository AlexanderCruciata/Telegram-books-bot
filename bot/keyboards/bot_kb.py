from aiogram.utils.keyboard import ReplyKeyboardBuilder
class Keyboards:
    @staticmethod
    async def user_keyboard():
        builder = ReplyKeyboardBuilder()
        builder.button(text="/books_list")
        builder.button(text="/random_book")
        builder.adjust(1)
        return builder.as_markup()
