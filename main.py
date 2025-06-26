from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 6846748073  # замени на свой Telegram ID
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
    "🛠 Настройки", "💼 Партнёрка"
)

# Главное меню UZ
MENU_UZ = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MENU_UZ.add(
    "📊 Indikatorlar", "📈 Strategiyalar",
    "🎓 Kurslar", "💬 Yordam",
    "📦 Mahsulot haqida", "💳 To‘lov",
    "🛠 Sozlamalar", "💼 Hamkorlik"
)

# Инлайн-кнопки продуктов
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

# Язык меню
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

# Оплата RU
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
        "💳 Способы оплаты:\n\n"
        "🇺🇿 Click: +998 95 112 00 42\n"
        "🌐 Payme: нажмите кнопку ниже\n"
        "💳 MasterCard (Anor Bank):\n"
        "`5477 3300 4324 0989`\n"
        "Имя: Anor Bank\n\n"
        "✅ После оплаты отправьте чек: @forex0042",
        reply_markup=kb, parse_mode="Markdown"
    )

# Оплата UZ
@dp.message_handler(lambda m: m.text == "💳 To‘lov")
async def pay_uz(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🔗 Payme orqali to‘lash", url="https://payme.uz/example"),
        InlineKeyboardButton("📋 Kartani nusxalash", callback_data="copy_card_uz"),
        InlineKeyboardButton("💸 To‘lov qilindi", callback_data="paid_uz"),
        InlineKeyboardButton("📩 Yordam", url="https://t.me/forex0042")
    )
    await message.answer(
        "💳 To‘lov usullari:\n\n"
        "🇺🇿 Click: +998 95 112 00 42\n"
        "🌐 Payme: quyidagi tugmani bosing\n"
        "💳 MasterCard (Anor Bank):\n"
        "`5477 3300 4324 0989`\n"
        "Ism: Anor Bank\n\n"
        "✅ To‘lovdan so‘ng chekni yuboring: @forex0042",
        reply_markup=kb, parse_mode="Markdown"
    )

# Inline: кнопка "купить"
@dp.callback_query_handler(lambda c: c.data == "buy_ru")
async def buy_ru(callback: types.CallbackQuery):
    await pay_ru(callback.message)

@dp.callback_query_handler(lambda c: c.data == "buy_uz")
async def buy_uz(callback: types.CallbackQuery):
    await pay_uz(callback.message)

# Inline: Назад
@dp.callback_query_handler(lambda c: c.data == "back_ru")
async def back_ru(callback: types.CallbackQuery):
    await callback.message.answer("🔙 Главное меню:", reply_markup=MENU_RU)

@dp.callback_query_handler(lambda c: c.data == "back_uz")
async def back_uz(callback: types.CallbackQuery):
    await callback.message.answer("🔙 Asosiy menyu:", reply_markup=MENU_UZ)

# Скопировать карту
@dp.callback_query_handler(lambda c: c.data in ["copy_card_ru", "copy_card_uz"])
async def copy_card(callback: types.CallbackQuery):
    await callback.message.answer("💳 5477 3300 4324 0989")

# Подтверждение оплаты + лог
@dp.callback_query_handler(lambda c: c.data in ["paid_ru", "paid_uz"])
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

# Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
# О ПРОДУКТЕ
@dp.message_handler(lambda m: m.text in ["📦 О продукте", "📦 Mahsulot haqida"])
async def about_product(message: types.Message):
    text = (
        "💼 <b>Что ты получаешь:</b>\n\n"
        "✅ Сигнальный индикатор (работает в TradingView)\n"
        "✅ Готовая стратегия\n"
        "✅ Видео‑курс от профи из США, Дубая, Малайзии\n"
        "✅ Постоянная поддержка 24/7\n\n"
        "🔥 <b>Ранее: 1300$</b>\n"
        "💰 <b>Сейчас: 290$</b>\n\n"
        "🚀 Получи доступ: @daromadgeniusbot"
    )
    await message.answer(text, parse_mode="HTML")


# ПАРТНЁРКА
@dp.message_handler(lambda m: m.text in ["💼 Партнёрка", "💼 Hamkorlik"])
async def partner_program(message: types.Message):
    text = (
        "🤝 <b>Партнёрская программа:</b>\n\n"
        "🎁 Пригласи 3 друзей — получи индикатор бесплатно\n"
        "🔗 Уникальная реферальная ссылка (скоро будет)\n"
        "📩 Связь: @forex0042\n\n"
        "📊 Статус: Ваша заявка обрабатывается..."
    )
    await message.answer(text, parse_mode="HTML")


# НАСТРОЙКИ
@dp.message_handler(lambda m: m.text in ["🛠 Настройки", "🛠 Sozlamalar"])
async def settings(message: types.Message):
    user_id = message.from_user.id
    text = (
        f"⚙️ <b>Настройки</b>\n\n"
        f"🆔 Ваш Telegram ID: <code>{user_id}</code>\n"
        f"🌐 Язык: Русский\n"
        f"📎 Версия бота: v1.0\n\n"
        f"💬 Поддержка: @forex0042"
    )
    await message.answer(text, parse_mode="HTML")
