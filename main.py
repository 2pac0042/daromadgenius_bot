from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import logging
import os

API_TOKEN = os.getenv("7481276211:AAFtUF5vKB4PFYiXZq1wYvOqhq61ox2xVoM")
if not API_TOKEN:
    raise ValueError("\u274c BOT_TOKEN \u043d\u0435 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d \u0432 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043e\u043a\u0440\u0443\u0436\u0435\u043d\u0438\u044f Railway")

ADMIN_ID = 6846748073
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

LANGUAGE_KEYBOARD = types.ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGE_KEYBOARD.add("\U0001F1F7\U0001F1FA Русский", "\U0001F1FA\U0001F1FF O'zbekcha")

MENU_RU = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MENU_RU.add("\U0001F4CA Индикаторы", "\U0001F4C8 Стратегии",
           "\U0001F393 Курсы", "\U0001F4AC Поддержка",
           "\U0001F4E6 О продукте", "\U0001F4B3 Оплатить",
           "\U0001F6E0 Настройки", "\U0001F4BC Партнёрка")

MENU_UZ = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MENU_UZ.add("\U0001F4CA Indikatorlar", "\U0001F4C8 Strategiyalar",
           "\U0001F393 Kurslar", "\U0001F4AC Yordam",
           "\U0001F4E6 Mahsulot haqida", "\U0001F4B3 To\u2018lov",
           "\U0001F6E0 Sozlamalar", "\U0001F4BC Hamkorlik")

product_buttons_ru = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("\U0001F6D2 Купить", callback_data="buy_ru"),
    InlineKeyboardButton("\U0001F519 Назад", callback_data="back_ru")
)

product_buttons_uz = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("\U0001F6D2 Xarid qilish", callback_data="buy_uz"),
    InlineKeyboardButton("\U0001F519 Orqaga", callback_data="back_uz")
)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("\U0001F44B Добро пожаловать! / Xush kelibsiz!\nВыберите язык:", reply_markup=LANGUAGE_KEYBOARD)

@dp.message_handler(lambda m: m.text == "\U0001F1F7\U0001F1FA Русский")
async def ru_menu(message: types.Message):
    await message.answer("\U0001F1F7\U0001F1FA Меню:", reply_markup=MENU_RU)

@dp.message_handler(lambda m: m.text == "\U0001F1FA\U0001F1FF O'zbekcha")
async def uz_menu(message: types.Message):
    await message.answer("\U0001F1FA\U0001F1FF Menyu:", reply_markup=MENU_UZ)

@dp.message_handler(lambda m: m.text in ["\U0001F4CA Индикаторы", "\U0001F4CA Indikatorlar"])
async def indicators(message: types.Message):
    await message.answer("\U0001F4CA Индикатор: 25$/250,000 so'm\n\U0001F4CC Чек: @forex0042", reply_markup=product_buttons_ru if message.text.startswith("\U0001F1F7") else product_buttons_uz)

@dp.message_handler(lambda m: m.text in ["\U0001F4C8 Стратегии", "\U0001F4C8 Strategiyalar"])
async def strategies(message: types.Message):
    await message.answer("\U0001F4C8 Стратегия: 35$/350,000 so'm\n\U0001F4CC Чек: @forex0042", reply_markup=product_buttons_ru if message.text.startswith("\U0001F1F7") else product_buttons_uz)

@dp.message_handler(lambda m: m.text in ["\U0001F393 Курсы", "\U0001F393 Kurslar"])
async def courses(message: types.Message):
    await message.answer_document(open("Технический_анализ_для_начинающих.pdf", "rb"))
    await message.answer("\U0001F393 Курс: 290$/3 100 000 so'm\n\U0001F4CC Чек: @forex0042", reply_markup=product_buttons_ru if message.text.startswith("\U0001F1F7") else product_buttons_uz)

if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
