from aiogram import Bot, Dispatcher, executor, types
import logging
import os

# Инициализация
API_TOKEN = os.getenv("BOT_TOKEN")  # Установишь в Railway или .env
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

# Старт
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать! / Xush kelibsiz!\n\nВыберите язык / Tilni tanlang:",
        reply_markup=LANGUAGE_KEYBOARD
    )

# Языки
@dp.message_handler(lambda m: m.text == "🇷🇺 Русский")
async def menu_ru(message: types.Message):
    await message.answer("Вы выбрали 🇷🇺 Русский. Меню:", reply_markup=MENU_RU)

@dp.message_handler(lambda m: m.text == "🇺🇿 O'zbekcha")
async def menu_uz(message: types.Message):
    await message.answer("Siz 🇺🇿 O'zbek tilini tanladingiz. Menyu:", reply_markup=MENU_UZ)

# RU Курсы
@dp.message_handler(lambda m: m.text == "🎓 Курсы")
async def ru_courses(message: types.Message):
    await message.answer(
        "🎓 Премиум курс по трейдингу & инвестированию\n"
        "🔹 Авторская методика от экспертов Wall Street\n"
        "🔹 Стратегии BlackRock и Vanguard\n"
        "🔹 Тактики, психология, риск-менеджмент\n"
        "🔹 Видеоуроки + PDF + кейсы\n\n"
        "💰 Цена: 700 $\n"
        "📌 Отправьте чек после оплаты в: @daromadgenius_support\n"
        "✅ После подтверждения вы получите курс."
    )

# UZ Курсы
@dp.message_handler(lambda m: m.text == "🎓 Kurslar")
async def uz_courses(message: types.Message):
    await message.answer(
        "🎓 Premium treyding va investitsiya kursi\n"
        "🔹 Wall Street metodikasi\n"
        "🔹 BlackRock / Vanguard strategiyalari\n"
        "🔹 Psixologiya, risk menejment\n"
        "🔹 Video + PDF + misollar\n\n"
        "💰 Narxi: 9 100 000 so‘m\n"
        "📌 Chekni yuboring: @daromadgenius_support\n"
        "✅ Tasdiqlangandan so'ng kurs yuboriladi."
    )

# RU Инфо
@dp.message_handler(lambda m: m.text == "📊 Индикаторы")
async def ru_indicators(message: types.Message):
    await message.answer("📊 Индикатор: 25 $")

@dp.message_handler(lambda m: m.text == "📈 Стратегии")
async def ru_strategies(message: types.Message):
    await message.answer("📈 Стратегия: 35 $")

# UZ Инфо
@dp.message_handler(lambda m: m.text == "📊 Indikatorlar")
async def uz_indicators(message: types.Message):
    await message.answer("📊 Indikator: 250,000 so’m")

@dp.message_handler(lambda m: m.text == "📈 Strategiyalar")
async def uz_strategies(message: types.Message):
    await message.answer("📈 Strategiya: 350,000 so’m")

# Валюта
@dp.message_handler(lambda m: m.text in ["💰 Валюта: USD ($)", "💰 Valyuta: UZS (so'm)"])
async def currency_info(message: types.Message):
    await message.answer("💡 Цены указаны в выбранной валюте. Свяжитесь с поддержкой для пересчета.")

# --- РУЧНАЯ ВЫДАЧА КУРСА — ТОЛЬКО ДЛЯ ТЕБЯ ---
@dp.message_handler(commands=["send_course"])
async def admin_send_course(message: types.Message):
    admin_id = 6846748073  # <- Твой Telegram user ID
    if message.from_user.id == admin_id:
        await message.reply("📥 Отправляю курс...")
        await bot.send_document(chat_id=message.chat.id, document="YOUR_FILE_ID_HERE")
    else:
        await message.reply("⛔️ У вас нет доступа к этой команде.")

# Запуск
if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
