import logging
from func_val import get_exchangeRate

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6145339012:AAGH-5h9PbZJCIqhUc8yGxEAqL5dkey7sao'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Bu Vallyutalar kursini ko'rsatib beruvchi bot")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Kommandalar ro'yxatidan birini tanlang!")


@dp.message_handler(commands=['usd_uzs'])
async def usdToUzs(message: types.Message):
    sum = get_exchangeRate()
    await message.answer(f"1 dollar {sum} so'm")


@dp.message_handler(commands=['rub_uzs'])
async def rubl_to_uzs(msg: types.Message):
    summa = get_exchangeRate('RUB', "UZS")
    await msg.answer(f"1 rubl {summa} so'm")


@dp.message_handler(commands=['eur_uzs'])
async def rubl_to_uzs(msg: types.Message):
    summa = get_exchangeRate('EUR', "UZS")
    await msg.answer(f"1 yevro {summa} so'm")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
