from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7056909516:AAFlIVW4O0ESwDAmlUXhvace5yQ0Yb3gCks')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открытьь вбе страницу', web_app=WebAppInfo(url='https://www.youtube.com/watch?v=N3yaDkk3o4k')))
    await message.answer('Привет мой друг!', reply_markup=markup)

executor.start_polling(dp)