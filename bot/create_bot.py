from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
import os

TOKEN = ""
BOT_PATH = os.getcwd()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
router = Router()
dp = Dispatcher()
