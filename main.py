
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import dp
from handlers.basic import (start, help, myinfo, picture)
from handlers.products import (show_products,shoes)


# from dotenv import load_dotenv
# from os import getenv
# import random


if __name__=="__main__":
    print(__name__)
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help, commands=["help"])
    dp.register_message_handler(myinfo, commands=["myinfo"])
    dp.register_message_handler(picture, commands=["picture"])
    dp.register_message_handler(show_products, commands=["products"])
    dp.register_message_handler(shoes, Text(startswith="Kids shoes"))
    dp.register_callback_query_handler(show_products, Text(equals="Welcome!"))
    executor.start_polling(dp)







