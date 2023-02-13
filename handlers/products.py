from aiogram import types
from config import bot


kb = types.ReplyKeyboardMarkup()
kb.add(
    types.KeyboardButton("Обувь")
)
kb.add(
    types.KeyboardButton("Одежда")
)
kb.add(
    types.KeyboardButton("Детская одежда")
)

# async def show_products(message:types.Message):
#     chat_id = message.from_user.id
#     await bot.send_message(
#         chat_id=chat_id,
#         text="Привет привет",
#         reply_markup=kb
#     )

async def show_products(call: types.CallbackQuery):
    await call.message.answer("Welcome, guest!")

async def shoes(message:types.Message):
    await message.reply("У нас закончились обувь вашего размера")