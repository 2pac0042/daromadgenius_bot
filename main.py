from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import logging

# 🔑 Вставь сюда свой токен
API_TOKEN = "7481276211:AAEcf-ZJGUvmQxb99FpN_9SOQpxfCwwzMHw"
ADMIN_ID = 6846748073  # Заменить на свой Telegram ID

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# 🔤 Выбор языка
LANGUAGE_KEYBOARD = types.ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGE_KEYBOARD.add("🇷🇺 Русский", "🇺🇿 O'zbekcha")

# 🇷🇺 Меню
MENU_RU = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MENU_RU.add(
    "📊 Индикаторы", "📈 Стратегии",
    "🎓 Курсы", "💬 Поддержка",
    "📦 О продукте", "💳 Оплатить",
    "🛠 Настройки", "💼 Партнёрка"
)

# 🇺🇿 Меню
MENU_UZ = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MENU_UZ.add(
    "📊 Indikatorlar", "📈 Strategiyalar",
    "🎓 Kurslar", "💬 Yordam",
    "📦 Mahsulot haqida", "💳 To‘lov",
    "🛠 Sozlamalar", "💼 Hamkorlik"
)

# 📦 Инлайн кнопки для покупки
product_buttons_ru = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("🛒 Купить", callback_data="buy_ru"),
    InlineKeyboardButton("🔙 Назад", callback_data="back_ru")
)
product_buttons_uz = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("🛒 Xarid qilish", callback_data="buy_uz"),
    InlineKeyboardButton("🔙 Orqaga", callback_data="back_uz")
)

# /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("👋 Добро пожаловать! / Xush kelibsiz!\nВыберите язык:", reply_markup=LANGUAGE_KEYBOARD)

# Выбор языка
@dp.message_handler(lambda m: m.text == "🇷🇺 Русский")
async def ru_menu(message: types.Message):
    await message.answer("🇷🇺 Меню:", reply_markup=MENU_RU)

@dp.message_handler(lambda m: m.text == "🇺🇿 O'zbekcha")
async def uz_menu(message: types.Message):
    await message.answer("🇺🇿 Menyu:", reply_markup=MENU_UZ)

# Индикаторы / Стратегии
@dp.message_handler(lambda m: m.text in ["📊 Индикаторы", "📊 Indikatorlar"])
async def indicators(message: types.Message):
    await message.answer("📊 Индикатор: 25$\n📎 Чек: @forex0042", reply_markup=product_buttons_ru if "Русский" in message.text else product_buttons_uz)

@dp.message_handler(lambda m: m.text in ["📈 Стратегии", "📈 Strategiyalar"])
async def strategies(message: types.Message):
    await message.answer("📈 Стратегия: 35$\n📎 Чек: @forex0042", reply_markup=product_buttons_ru if "Русский" in message.text else product_buttons_uz)

@dp.message_handler(lambda m: m.text in ["🎓 Курсы", "🎓 Kurslar"])
async def courses(message: types.Message):
    await message.answer("🎓 Курс: 290$\n📎 Чек: @forex0042", reply_markup=product_buttons_ru if "Русский" in message.text else product_buttons_uz)

# О продукте
@dp.message_handler(lambda m: m.text in ["📦 О продукте", "📦 Mahsulot haqida"])
async def about(message: types.Message):
    await message.answer(
        "💼 <b>Что ты получаешь:</b>\n\n"
        "✅ Индикатор\n✅ Стратегия\n✅ Видео-курс\n✅ Поддержка 24/7\n\n"
        "🔥 <b>Ранее: 1300$</b>\n💰 <b>Сейчас: 290$</b>\n\n"
        "🚀 Доступ: @daromadgeniusbot", parse_mode="HTML"
    )

# Партнёрка
@dp.message_handler(lambda m: m.text in ["💼 Партнёрка", "💼 Hamkorlik"])
async def partner(message: types.Message):
    await message.answer(
        "🤝 <b>Партнёрка:</b>\n\n🎁 Пригласи 3 друзей — получи индикатор бесплатно\n"
        "🔗 Реферальная ссылка (скоро)\n"
        "📩 Связь: @forex0042", parse_mode="HTML"
    )

# Настройки
@dp.message_handler(lambda m: m.text in ["🛠 Настройки", "🛠 Sozlamalar"])
async def settings(message: types.Message):
    await message.answer(
        f"⚙️ <b>Настройки</b>\n\n🌐 Язык: авто\n📁 Версия: 1.0\n📅 Дата: {datetime.now().strftime('%Y-%m-%d')}\n👤 ID: <code>{message.from_user.id}</code>",
        parse_mode="HTML"
    )

# Оплата
@dp.message_handler(lambda m: m.text in ["💳 Оплатить", "💳 To‘lov"])
async def pay(message: types.Message):
    lang = "ru" if "Оплатить" in message.text else "uz"
    kb = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton("🔗 Перейти на Payme", url="https://payme.uz/example"),
        InlineKeyboardButton("📋 Скопировать карту", callback_data="copy_card"),
        InlineKeyboardButton("💸 Я оплатил", callback_data=f"paid_{lang}"),
        InlineKeyboardButton("📩 Поддержка", url="https://t.me/forex0042")
    )
    await message.answer(
        "💳 Способы оплаты:\n\n"
        "🇺🇿 Click: +998 95 112 00 42\n"
        "🌐 Payme: по кнопке ниже\n"
        "💳 MasterCard: 5477 3300 4324 0989\n\n"
        "✅ После оплаты отправьте чек в @forex0042",
        reply_markup=kb
    )

# Подтверждение оплаты
@dp.callback_query_handler(lambda c: c.data.startswith("paid_"))
async def paid_confirm(callback: types.CallbackQuery):
    lang = "RU" if "ru" in callback.data else "UZ"
    user = callback.from_user
    time = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    log = f"{time} {lang} - {user.full_name} ({user.id}) нажал 'Оплатил'"
    await bot.send_message(ADMIN_ID, log)
    await callback.message.answer("📩 Спасибо! Чек отправьте в @forex0042")

# Скопировать карту
@dp.callback_query_handler(lambda c: c.data == "copy_card")
async def copy_card(callback: types.CallbackQuery):
    await callback.message.answer("💳 5477 3300 4324 0989")

# Инлайн кнопки
@dp.callback_query_handler(lambda c: c.data == "buy_ru")
async def buy_ru(callback: types.CallbackQuery):
    await pay(callback.message)

@dp.callback_query_handler(lambda c: c.data == "buy_uz")
async def buy_uz(callback: types.CallbackQuery):
    await pay(callback.message)

@dp.callback_query_handler(lambda c: c.data == "back_ru")
async def back_ru(callback: types.CallbackQuery):
    await callback.message.answer("🔙 Главное меню", reply_markup=MENU_RU)

@dp.callback_query_handler(lambda c: c.data == "back_uz")
async def back_uz(callback: types.CallbackQuery):
    await callback.message.answer("🔙 Asosiy menyu", reply_markup=MENU_UZ)

# ▶️ Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



