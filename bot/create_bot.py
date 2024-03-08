from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
import os

TOKEN = "7199178671:AAGYvJTPeW9XXcuS0l_wQ1m8OQiM3BUFXSY"
BOT_PATH = os.getcwd()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
router = Router()
dp = Dispatcher()
