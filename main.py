from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# --- Клавиатура выбора языка ---
LANGUAGE_KEYBOARD = types.ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGE_KEYBOARD.add("🇷🇺 Русский", "🇺🇿 O'zbekcha")

# --- Меню RU ---
MENU_RU = types.ReplyKeyboardMarkup(resize_keyboard=True)
MENU_RU.add("📊 Индикаторы", "📈 Стратегии", "🎓 Курсы")
MENU_RU.add("💰 Валюта: USD ($)")

# --- Меню UZ ---
MENU_UZ = types.ReplyKeyboardMarkup(resize_keyboard=True)
MENU_UZ.add("📊 Indikatorlar", "📈 Strategiyalar", "🎓 Kurslar")
MENU_UZ.add("💰 Valyuta: UZS (so'm)")

# --- Инлайн-кнопки RU ---
product_buttons_ru = InlineKeyboardMarkup(row_width=2)
product_buttons_ru.add(
    InlineKeyboardButton("🛒 Купить", callback_data="buy_ru"),
    InlineKeyboardButton("🔙 Назад", callback_data="back_ru")
)

# --- Инлайн-кнопки UZ ---
product_buttons_uz = InlineKeyboardMarkup(row_width=2)
product_buttons_uz.add(
    InlineKeyboardButton("🛒 Xarid qilish", callback_data="buy_uz"),
    InlineKeyboardButton("🔙 Orqaga", callback_data="back_uz")
)

# --- START ---
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать! / Xush kelibsiz!\n\nВыберите язык / Tilni tanlang:",
        reply_markup=LANGUAGE_KEYBOARD
    )

# --- Язык RU ---
@dp.message_handler(lambda m: m.text == "🇷🇺 Русский")
async def menu_ru(message: types.Message):
    await message.answer("Вы выбрали 🇷🇺 Русский. Меню:", reply_markup=MENU_RU)

# --- Язык UZ ---
@dp.message_handler(lambda m: m.text == "🇺🇿 O'zbekcha")
async def menu_uz(message: types.Message):
    await message.answer("Siz 🇺🇿 O'zbek tilini tanladingiz. Menyu:", reply_markup=MENU_UZ)

# --- RU КУРСЫ ---
@dp.message_handler(lambda m: m.text == "🎓 Курсы")
async def ru_courses(message: types.Message):
    await message.answer(
        "🎓 Премиум курс по трейдингу & инвестированию\n"
        "🔹 Авторская методика от экспертов Wall Street\n"
        "🔹 Стратегии BlackRock и Vanguard\n"
        "🔹 Тактики, психология, риск-менеджмент\n"
        "🔹 Видеоуроки + PDF + кейсы\n\n"
        "💰 Цена: 700 $\n"
        "📌 Отправьте чек после оплаты в: @forex0042\n"
        "✅ После подтверждения вы получите курс.",
        reply_markup=product_buttons_ru
    )

@dp.message_handler(lambda m: m.text == "📈 Стратегии")
async def ru_strategies(message: types.Message):
    await message.answer(
        "📈 Стратегия: 35 $\n📌 Чек отправьте: @forex0042",
        reply_markup=product_buttons_ru
    )

@dp.message_handler(lambda m: m.text == "📊 Индикаторы")
async def ru_indicators(message: types.Message):
    await message.answer(
        "📊 Индикатор: 25 $\n📌 Чек отправьте: @forex0042 ",
        reply_markup=product_buttons_ru
    )

# --- UZ KURSLAR ---
@dp.message_handler(lambda m: m.text == "🎓 Kurslar")
async def uz_courses(message: types.Message):
    await message.answer(
        "🎓 Premium treyding va investitsiya kursi\n"
        "🔹 Wall Street metodikasi\n"
        "🔹 BlackRock / Vanguard strategiyalari\n"
        "🔹 Psixologiya, risk menejment\n"
        "🔹 Video + PDF + misollar\n\n"
        "💰 Narxi: 3 100 000 so‘m\n"
        "📌 Chekni yuboring: @forex0042\n"
        "✅ Tasdiqlangandan so'ng kurs yuboriladi.",
        reply_markup=product_buttons_uz
    )

@dp.message_handler(lambda m: m.text == "📈 Strategiyalar")
async def uz_strategiyalar(message: types.Message):
    await message.answer(
        "📈 Strategiya: 350,000 so'm\n📌 Chekni yuboring: @forex0042",
        reply_markup=product_buttons_uz
    )

@dp.message_handler(lambda m: m.text == "📊 Indikatorlar")
async def uz_indicators(message: types.Message):
    await message.answer(
        "📊 Indikator: 250,000 so'm\n📌 Chekni yuboring: @forex0042",
reply_markup=product_buttons_uz
    )

# --- Валюта информативно ---
@dp.message_handler(lambda m: m.text in ["💰 Валюта: USD ($)", "💰 Valyuta: UZS (so'm)"])
async def currency_info(message: types.Message):
    await message.answer("💱 Цены указаны в выбранной валюте. Свяжитесь с поддержкой для пересчета.")

# --- CALLBACKS RU ---
@dp.callback_query_handler(lambda c: c.data == "buy_ru")
async def buy_ru(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("💳 Для покупки отправьте чек в: @forex0042")

@dp.callback_query_handler(lambda c: c.data == "back_ru")
async def back_ru(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("🔙 Главное меню:", reply_markup=MENU_RU)

# --- CALLBACKS UZ ---
@dp.callback_query_handler(lambda c: c.data == "buy_uz")
async def buy_uz(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("💳 To‘lov uchun chekni @forex0042 ga yuboring.")

@dp.callback_query_handler(lambda c: c.data == "back_uz")
async def back_uz(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("🔙 Asosiy menyu:", reply_markup=MENU_UZ)

# --- АДМИН-КОМАНДА: вручную отправить курс ---
@dp.message_handler(commands=["send_course"])
async def admin_send_course(message: types.Message):
    admin_id = 6846748073  # ← Твой Telegram ID
    if message.from_user.id == admin_id:
        await message.reply("📥 Отправляю курс...")
        await bot.send_document(chat_id=message.chat.id, document="YOUR_FILE_ID_HERE")
    else:
        await message.reply("⛔ У вас нет доступа к этой команде.")
