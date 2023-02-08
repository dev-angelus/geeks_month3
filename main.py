from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv
import random

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    user = message.from_user.full_name
    await message.answer(
        f'Hello, {user}!'
    )

@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(
        """
        /start - приветствие
        /help - список команд
        /myinfo - данные пользователя
        /picture - картинка из папки images
        """
    )
@dp.message_handler(commands=["myinfo"])
async def myinfo(message: types.Message):
    user = message.from_user.full_name
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    await message.answer(
        f'Username: {user}\n'
        f'User ID: {user_id}\n'
        f'User first name: {first_name}\n'
        f'User last name: {last_name}\n'
    )
    # await message.delete()
@dp.message_handler(commands=["picture"])
async def picture(message: types.Message):
    photos = ['/images_cat/cat.webp','/images_cat/snowleo.jpeg','/images_cat/cheetah.jpeg','/images_cat/jaguar.jpeg']
    with open(random.choice(photos), 'rb') as photos:
        await message.answer_photo(
            photo = photos,
            caption = 'cat family'
        )

@dp.message_handler()
async def echo(message: types.Message):
    text = len(message.text)
    if text>3:
        await message.answer(
            f'{message.text.upper()}'
        )
    else:
        pass

executor.start_polling(dp)







