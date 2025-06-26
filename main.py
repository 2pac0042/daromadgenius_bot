from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import logging
import os

# Получаем токен из переменных окружения
API_TOKEN = os.getenv("7481276211:AAEcf-ZJGUvmQxb99FpN_9SOQpxfCwwzMHw")
if not API_TOKEN:
    raise ValueError("7481276211:AAEcf-ZJGUvmQxb99FpN_9SOQpxfCwwzMHw")

ADMIN_ID = 6846748073  # Замени на свой Telegram ID
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Клавиатуры
LANGUAGE_KEYBOARD = types.ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGE_KEYBOARD.add("🇷🇺 Русский", "🇺🇿 O'zbekcha")

MENU_RU = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    "📊 Индикаторы", "📈 Стратегии",
    "🎓 Курсы", "💬 Поддержка",
    "📦 О продукте", "💳 Оплатить",
    "🛠 Настройки", "💼 Партнёрка"
)

MENU_UZ = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    "📊 Indikatorlar", "📈 Strategiyalar",
    "🎓 Kurslar", "💬 Yordam",
    "📦 Mahsulot haqida", "💳 To‘lov",
    "🛠 Sozlamalar", "💼 Hamkorlik"
)

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

@dp.message_handler(lambda m: m.text == "🇷🇺 Русский")
async def ru_menu(message: types.Message):
    await message.answer("🇷🇺 Меню:", reply_markup=MENU_RU)

@dp.message_handler(lambda m: m.text == "🇺🇿 O'zbekcha")
async def uz_menu(message: types.Message):
    await message.answer("🇺🇿 Menyu:", reply_markup=MENU_UZ)

# Категории
@dp.message_handler(lambda m: m.text in ["📊 Индикаторы", "📊 Indikatorlar"])
async def indicators(message: types.Message):
    if message.text == "📊 Индикаторы":
        await message.answer("📊 Индикатор: 25$\n📌 Чек: @forex0042", reply_markup=product_buttons_ru)
    else:
        await message.answer("📊 Indikator: 250 000 so'm\n📌 Chek: @forex0042", reply_markup=product_buttons_uz)

@dp.message_handler(lambda m: m.text in ["📈 Стратегии", "📈 Strategiyalar"])
async def strategies(message: types.Message):
    if message.text == "📈 Стратегии":
        await message.answer("📈 Стратегия: 35$\n📌 Чек: @forex0042", reply_markup=product_buttons_ru)
    else:
        await message.answer("📈 Strategiya: 350 000 so'm\n📌 Chek: @forex0042", reply_markup=product_buttons_uz)

@dp.message_handler(lambda m: m.text in ["🎓 Курсы", "🎓 Kurslar"])
async def courses(message: types.Message):
    if message.text == "🎓 Курсы":
        await message.answer("🎓 Курс: 290$\n📌 Чек: @forex0042", reply_markup=product_buttons_ru)
    else:
        await message.answer("🎓 Kurs: 3 100 000 so'm\n📌 Chek: @forex0042", reply_markup=product_buttons_uz)

# Оплата
@dp.message_handler(lambda m: m.text in ["💳 Оплатить", "💳 To‘lov"])
async def pay(message: types.Message):
    lang = "ru" if message.text == "💳 Оплатить" else "uz"
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🔗 Payme", url="https://payme.uz/example"),
        InlineKeyboardButton("📋 Скопировать карту" if lang == "ru" else "📋 Kartani nusxalash", callback_data=f"copy_card_{lang}"),
        InlineKeyboardButton("💸 Я оплатил" if lang == "ru" else "💸 To‘lov qilindi", callback_data=f"paid_{lang}"),
        InlineKeyboardButton("📩 Поддержка" if lang == "ru" else "📩 Yordam", url="https://t.me/forex0042")
    )
    text = (
        "💳 Способы оплаты:\n\n"
        "🇺🇿 Click: +998 95 112 00 42\n"
        "🌐 Payme: нажмите кнопку ниже\n"
        "💳 MasterCard (TBC BANK):\n"
        "`9860350147273881`\n"
        "Имя: TBC BANK\n\n"
        "✅ После оплаты отправьте чек: @forex0042" if lang == "ru" else
        "💳 To‘lov usullari:\n\n"
        "🇺🇿 Click: +998 95 112 00 42\n"
        "🌐 Payme: quyidagi tugmani bosing\n"
        "💳 MasterCard (TBC BANK):\n"
        "`9860350147273881`\n"
        "Ism: Anor Bank\n\n"
        "✅ To‘lovdan so‘ng chekni yuboring: @forex0042"
    )
    await message.answer(text, reply_markup=kb, parse_mode="Markdown")

# Inline кнопки
@dp.callback_query_handler(lambda c: c.data.startswith("buy_"))
async def buy(callback: types.CallbackQuery):
    if callback.data == "buy_ru":
        await pay(callback.message)
    else:
        await pay(callback.message)

@dp.callback_query_handler(lambda c: c.data.startswith("back_"))
async def back(callback: types.CallbackQuery):
    await callback.message.answer("🔙 Главное меню:" if callback.data == "back_ru" else "🔙 Asosiy menyu:",
                                  reply_markup=MENU_RU if callback.data == "back_ru" else MENU_UZ)

@dp.callback_query_handler(lambda c: c.data.startswith("copy_card"))
async def copy_card(callback: types.CallbackQuery):
    await callback.message.answer("💳 9860350147273881")

@dp.callback_query_handler(lambda c: c.data.startswith("paid_"))
async def paid_confirm(callback: types.CallbackQuery):
    user = callback.from_user
    lang = "RU" if callback.data == "paid_ru" else "UZ"
    time = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    log_text = f"{time} {lang} - {user.full_name} ({user.id}) нажал 'Оплатил'\n"

    try:
        with open("purchase_logs.txt", "a", encoding="utf-8") as f:
            f.write(log_text)
    except Exception as e:
        logging.error(f"Ошибка при записи лога: {e}")

    await bot.send_message(chat_id=ADMIN_ID, text=log_text)
    await callback.message.answer("📩 Спасибо! Чек отправьте в @forex0042 для подтверждения.")

# О продукте
@dp.message_handler(lambda m: m.text in ["📦 О продукте", "📦 Mahsulot haqida"])
async def about_product(message: types.Message):
    await message.answer(
        "💼 <b>Что ты получаешь:</b>\n\n"
        "✅ Индикатор (TradingView)\n"
        "✅ Готовая стратегия\n"
        "✅ Видео-курс от профессионалов\n"
        "✅ Поддержка 24/7\n\n"
        "🔥 <b>Ранее: 1300$</b>\n"
        "💰 <b>Сейчас: 290$</b>\n\n"
        "🚀 Получи доступ: @daromadgenius_bot",
        parse_mode="HTML"
    )

# Партнёрка
@dp.message_handler(lambda m: m.text in ["💼 Партнёрка", "💼 Hamkorlik"])
async def partner(message: types.Message):
    await message.answer(
        "🤝 <b>Партнёрская программа:</b>\n\n"
        "🎁 Пригласи 3 друзей — получи индикатор бесплатно\n"
        "🔗 Реферальная ссылка (скоро будет)\n"
        "📩 Связь: @forex0042",
        parse_mode="HTML"
    )

# Настройки
@dp.message_handler(lambda m: m.text in ["🛠 Настройки", "🛠 Sozlamalar"])
async def settings(message: types.Message):
    user_id = message.from_user.id
    await message.answer(
        f"⚙️ <b>Настройки</b>\n\n"
        f"🆔 Ваш Telegram ID: <code>{user_id}</code>\n"
        f"🌐 Язык: Автоопределение\n"
        f"📎 Версия бота: v1.0\n\n"
        f"💬 Поддержка: @forex0042",
        parse_mode="HTML"
    )

# Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


