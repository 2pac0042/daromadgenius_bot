from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import logging

API_TOKEN = "8040390729:AAEr0iktkA-6yLBrtgGOwxFR6QbA7gl4F4M"  # токен прямо в коде
ADMIN_ID = 6846748073  # Telegram ID

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Главное меню RU
MENU_RU = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MENU_RU.add(
    "📊 Индикаторы", "📈 Стратегии",
    "🎓 Курсы", "💬 Поддержка",
    "📦 О продукте", "💳 Оплатить",
    "🛠 Настройки", "💼 Партнёрка"
)

# Инлайн-кнопки продуктов
product_buttons_ru = InlineKeyboardMarkup(row_width=2)
product_buttons_ru.add(
    InlineKeyboardButton("🛒 Купить", callback_data="buy_ru"),
    InlineKeyboardButton("🔙 Назад", callback_data="back_ru")
)

# /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("👋 Добро пожаловать!
", reply_markup=MENU_RU)

# Категории RU
@dp.message_handler(lambda m: m.text == "📊 Индикаторы")
async def indicators_ru(message: types.Message):
    await message.answer("📊 Индикатор: 25 $
📌 Чек отправьте: @forex0042", reply_markup=product_buttons_ru)

@dp.message_handler(lambda m: m.text == "📈 Стратегии")
async def strategies_ru(message: types.Message):
    await message.answer("📈 Стратегия: 35 $
📌 Чек отправьте: @forex0042", reply_markup=product_buttons_ru)

@dp.message_handler(lambda m: m.text == "🎓 Курсы")
async def courses_ru(message: types.Message):
    await message.answer("🎓 Курс: 290 $
📌 Чек отправьте: @forex0042", reply_markup=product_buttons_ru)

# О ПРОДУКТЕ
@dp.message_handler(lambda m: m.text == "📦 О продукте")
async def about_product(message: types.Message):
    text_ru = (
        "📦 Это не просто курс. Это 🔥 полный набор:

"
        "✔️ Индикатор для точного входа
"
        "✔️ Стратегии, протестированные на рынке
"
        "✔️ Видеоуроки от профессионалов
"
        "✔️ Постоянная поддержка

"
        "💥 Всё это — по спеццене: ~1300$~ 👉 290$
"
        "🚀 Только для избранных. Торопись!"
    )
    await message.answer(text_ru)

# Партнёрка
@dp.message_handler(lambda m: m.text == "💼 Партнёрка")
async def partnership(message: types.Message):
    await message.answer(
        "💼 Партнёрская программа:

"
        "👥 Приглашай друзей и трейдеров
"
        "💰 Получай 20% от каждого заказа
"
        "📩 Подключение через @forex0042

"
        "⚠️ Только для активных и лояльных!"
    )

# Настройки
@dp.message_handler(lambda m: m.text == "🛠 Настройки")
async def settings(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
        InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data="lang_uz")
    )
    await message.answer("🌐 Выберите язык:", reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data.startswith("lang_"))
async def change_language(callback: types.CallbackQuery):
    lang = "Русский" if callback.data.endswith("ru") else "O'zbekcha"
    await callback.message.answer(f"✅ Язык изменён на: {lang}")

# Поддержка
@dp.message_handler(lambda m: m.text == "💬 Поддержка")
async def support(message: types.Message):
    await message.answer("📩 Все вопросы сюда: @forex0042")

# Оплата
@dp.message_handler(lambda m: m.text == "💳 Оплатить")
async def pay_ru(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🔗 Перейти на Payme", url="https://payme.uz/example"),
        InlineKeyboardButton("📋 Скопировать карту", callback_data="copy_card_ru"),
        InlineKeyboardButton("💸 Я оплатил", callback_data="paid_ru"),
        InlineKeyboardButton("📩 Поддержка", url="https://t.me/forex0042")
    )
    await message.answer(
        "💳 Способы оплаты:

"
        "🇺🇿 Click: +998 95 112 00 42
"
        "🌐 Payme: нажмите кнопку ниже
"
        "💳 MasterCard (Anor Bank):
"
        "`5477 3300 4324 0989`
"
        "Имя: Anor Bank

"
        "✅ После оплаты отправьте чек: @forex0042",
        reply_markup=kb, parse_mode="Markdown"
    )

# Callback кнопки
@dp.callback_query_handler(lambda c: c.data == "copy_card_ru")
async def copy_card(callback: types.CallbackQuery):
    await callback.message.answer("💳 5477 3300 4324 0989")

@dp.callback_query_handler(lambda c: c.data == "paid_ru")
async def paid_confirm(callback: types.CallbackQuery):
    user = callback.from_user
    time = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    log_text = f"{time} RU - {user.full_name} ({user.id}) нажал 'Оплатил'\n"
    with open("purchase_logs.txt", "a", encoding="utf-8") as f:
        f.write(log_text)
    await bot.send_message(chat_id=ADMIN_ID, text=log_text)
    await callback.message.answer("📩 Спасибо! Чек отправьте в @forex0042 для подтверждения.")

# Inline buy
@dp.callback_query_handler(lambda c: c.data == "buy_ru")
async def buy_ru(callback: types.CallbackQuery):
    await pay_ru(callback.message)

@dp.callback_query_handler(lambda c: c.data == "back_ru")
async def back_ru(callback: types.CallbackQuery):
    await callback.message.answer("🔙 Главное меню:", reply_markup=MENU_RU)

# Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)