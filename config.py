from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot)
