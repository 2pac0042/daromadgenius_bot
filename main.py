from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import logging
import os

API_TOKEN = os.getenv("7481276211:AAEcf-ZJGUvmQxb99FpN_9SOQpxfCwwzMHw")
ADMIN_ID = 6846748073  # Замени на свой Telegram ID
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Языковая клавиатура
LANGUAGE_KEYBOARD = types.ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGE_KEYBOARD.add("🇷🇺 Русский", "🇺🇿 O'zbekcha")

# Главное меню RU
MENU_RU = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MENU_RU.add(
    "📊 Индикаторы", "📈 Стратегии",
    "🎓 Курсы", "💬 Поддержка",
    "📦 О продукте", "💳 Оплатить",
    "🛠 Настройки", "💼 Партнёрка",
    "🎥 Видео", "❓ Вопросы"
)

# Главное меню UZ
MENU_UZ = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MENU_UZ.add(
    "📊 Indikatorlar", "📈 Strategiyalar",
    "🎓 Kurslar", "💬 Yordam",
    "📦 Mahsulot haqida", "💳 To‘lov",
    "🛠 Sozlamalar", "💼 Hamkorlik",
    "🎥 Video", "❓ Savollar"
)

# Инлайн-кнопки RU
product_buttons_ru = InlineKeyboardMarkup(row_width=2)
product_buttons_ru.add(
    InlineKeyboardButton("🛒 Купить", callback_data="buy_ru"),
    InlineKeyboardButton("🔙 Назад", callback_data="back_ru")
)

product_buttons_uz = InlineKeyboardMarkup(row_width=2)
product_buttons_uz.add(
    InlineKeyboardButton("🛒 Xarid qilish", callback_data="buy_uz"),
    InlineKeyboardButton("🔙 Orqaga", callback_data="back_uz")
)

# /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("👋 Добро пожаловать! / Xush kelibsiz!\nВыберите язык:", reply_markup=LANGUAGE_KEYBOARD)

@dp.message_handler(lambda m: m.text == "🇷🇺 Русский")
async def ru_menu(message: types.Message):
    await message.answer("🇷🇺 Меню:", reply_markup=MENU_RU)

@dp.message_handler(lambda m: m.text == "🇺🇿 O'zbekcha")
async def uz_menu(message: types.Message):
    await message.answer("🇺🇿 Menyu:", reply_markup=MENU_UZ)

# Категории RU
@dp.message_handler(lambda m: m.text == "📊 Индикаторы")
async def indicators_ru(message: types.Message):
    await message.answer("📊 Индикатор: 25 $\n📌 Чек отправьте: @forex0042", reply_markup=product_buttons_ru)

@dp.message_handler(lambda m: m.text == "📈 Стратегии")
async def strategies_ru(message: types.Message):
    await message.answer("📈 Стратегия: 35 $\n📌 Чек отправьте: @forex0042", reply_markup=product_buttons_ru)

@dp.message_handler(lambda m: m.text == "🎓 Курсы")
async def courses_ru(message: types.Message):
    await message.answer("🎓 Курс: 290 $\n📌 Чек отправьте: @forex0042", reply_markup=product_buttons_ru)

# Категории UZ
@dp.message_handler(lambda m: m.text == "📊 Indikatorlar")
async def indicators_uz(message: types.Message):
    await message.answer("📊 Indikator: 250,000 so’m\n📌 Chek yuboring: @forex0042", reply_markup=product_buttons_uz)

@dp.message_handler(lambda m: m.text == "📈 Strategiyalar")
async def strategies_uz(message: types.Message):
    await message.answer("📈 Strategiya: 350,000 so’m\n📌 Chek yuboring: @forex0042", reply_markup=product_buttons_uz)

@dp.message_handler(lambda m: m.text == "🎓 Kurslar")
async def courses_uz(message: types.Message):
    await message.answer("🎓 Kurs: 3 100 000 so’m\n📌 Chek yuboring: @forex0042", reply_markup=product_buttons_uz)

# О продукте
@dp.message_handler(lambda m: m.text in ["📦 О продукте", "📦 Mahsulot haqida"])
async def about_product(message: types.Message):
    text = (
        "💼 <b>Что ты получаешь:</b>\n\n"
        "✅ Сигнальный индикатор (работает в TradingView)\n"
        "✅ Готовая стратегия\n"
        "✅ Видеокурс от трейдеров США, Дубай, Малайзия\n"
        "✅ Постоянная поддержка 24/7\n\n"
        "🔥 <b>Ранее: 1300$</b>\n"
        "💰 <b>Сейчас: 290$</b>\n\n"
        "🚀 Получи доступ: @daromadgeniusbot"
    )
    await message.answer(text, parse_mode="HTML")

# Партнёрка
@dp.message_handler(lambda m: m.text in ["💼 Партнёрка", "💼 Hamkorlik"])
async def partner_program(message: types.Message):
    text = (
        "🤝 <b>Партнёрская программа:</b>\n\n"
        "🎁 Пригласи 3 друзей — получи индикатор бесплатно\n"
        "🔗 Уникальная ссылка (скоро будет)\n"
        "📩 Связь: @forex0042\n\n"
        "📊 Статус: Заявка обрабатывается..."
    )
    await message.answer(text, parse_mode="HTML")

# Настройки
@dp.message_handler(lambda m: m.text in ["🛠 Настройки", "🛠 Sozlamalar"])
async def settings(message: types.Message):
    user_id = message.from_user.id
    await message.answer(
        f"⚙️ <b>Настройки</b>\n\n"
        f"🆔 Ваш ID: <code>{user_id}</code>\n"
        f"📎 Версия: <b>v1.0 Premium</b>\n"
        f"💬 Поддержка: @forex0042", parse_mode="HTML"
    )

# Видео
@dp.message_handler(lambda m: m.text in ["🎥 Видео"])
async def show_video(message: types.Message):
    await message.answer("🎥 Демо видео Trade Genius Bot:\nhttps://youtu.be/example")

# Вопросы
@dp.message_handler(lambda m: m.text in ["❓ Вопросы", "❓ Savollar"])
async def faq(message: types.Message):
    await message.answer(
        "❓ Часто задаваемые вопросы:\n\n"
        "1. Это работает? — Да, доказано результатами.\n"
        "2. Где сигналы? — В индикаторе и курсах.\n"
        "3. Как оплатить? — Через Payme, Click, UzCard.\n"
        "4. Как получить? — После оплаты доступ откроется.",
    )

# Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


