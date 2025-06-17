from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
import os
API_TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# Языковая клавиатура
LANGUAGE_KEYBOARD = types.ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGE_KEYBOARD.add("🇷🇺 Русский", "🇺🇿 O'zbekcha")
# Главное меню
MENU_RU = types.ReplyKeyboardMarkup(resize_keyboard=True)
MENU_RU.add("📊 Индикаторы", "📈 Стратегии", "🎓 Курсы")
MENU_RU.add("💰 Валюта: USD ($)")
MENU_UZ = types.ReplyKeyboardMarkup(resize_keyboard=True)
MENU_UZ.add("📊 Indikatorlar", "📈 Strategiyalar", "🎓 Kurslar")
MENU_UZ.add("💰 Valyuta: UZS (so'm)")
# Инлайн-кнопки
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
# Команды
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("👋 Добро пожаловать! / Xush kelibsiz!\nВыберите язык:", reply_markup=LANGUAGE_KEYBOARD)
@dp.message_handler(lambda m: m.text == "🇷🇺 Русский")
async def ru_menu(message: types.Message):
    await message.answer("Вы выбрали 🇷🇺 Русский. Меню:", reply_markup=MENU_RU)
@dp.message_handler(lambda m: m.text == "🇺🇿 O'zbekcha")
async def uz_menu(message: types.Message):
    await message.answer("Siz 🇺🇿 O'zbek tilini tanladingiz. Menyu:", reply_markup=MENU_UZ)
# RU товары
@dp.message_handler(lambda m: m.text == "🎓 Курсы")
async def ru_courses(message: types.Message):
    await message.answer(
        "🎓 Премиум курс по трейдингу & инвестированию\n"
        "🔹 Авторская методика\n"
        "🔹 BlackRock и Vanguard\n"
        "🔹 Тактики, психология, риск-менеджмент\n"
        "🔹 Видеоуроки + PDF\n\n"
        "💰 700 $\n📌 Чек отправьте: @forex0042",
        reply_markup=product_buttons_ru
    )
@dp.message_handler(lambda m: m.text == "📈 Стратегии")
async def ru_strategies(message: types.Message):
    await message.answer("📈 Стратегия: 35 $\n📌 Чек отправьте: @forex0042", reply_markup=product_buttons_ru)

@dp.message_handler(lambda m: m.text == "📊 Индикаторы")
async def ru_indicators(message: types.Message):
    await message.answer("📊 Индикатор: 25 $\n📌 Чек отправьте: @forex0042", reply_markup=product_buttons_ru)
# UZ товары
@dp.message_handler(lambda m: m.text == "🎓 Kurslar")
async def uz_courses(message: types.Message):
    await message.answer(
        "🎓 Premium treyding va investitsiya kursi\n"
        "🔹 Wall Street metodikasi\n"
        "🔹 BlackRock/Vanguard strategiyasi\n"
        "🔹 Video + PDF + psixologiya\n\n"
        "💰 3 100 000 so’m\n📌 Chek yuboring: @forex0042",
        reply_markup=product_buttons_uz
    )
@dp.message_handler(lambda m: m.text == "📈 Strategiyalar")
async def uz_strategies(message: types.Message):
    await message.answer("📈 Strategiya: 350,000 so’m\n📌 Chek yuboring: @forex0042", reply_markup=product_buttons_uz)
@dp.message_handler(lambda m: m.text == "📊 Indikatorlar")
async def uz_indicators(message: types.Message):
    await message.answer("📊 Indikator: 250,000 so’m\n📌 Chek yuboring: @forex0042", reply_markup=product_buttons_uz)
# Инфо по валюте
@dp.message_handler(lambda m: m.text in ["💰 Валюта: USD ($)", "💰 Valyuta: UZS (so'm)"])
async def currency_info(message: types.Message):
    await message.answer("💱 Все цены указаны в выбранной валюте.")
# Callback RU
@dp.callback_query_handler(lambda c: c.data == "buy_ru")
async def buy_ru(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("💳 Отправьте чек в @forex0042")
@dp.callback_query_handler(lambda c: c.
data == "back_ru")
async def back_ru(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("🔙 Главное меню:", reply_markup=MENU_RU)
# Callback UZ
@dp.callback_query_handler(lambda c: c.data == "buy_uz")
async def buy_uz(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("💳 Chekni @forex0042 ga yuboring.")
@dp.callback_query_handler(lambda c: c.data == "back_uz")
async def back_uz(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("🔙 Asosiy menyu:", reply_markup=MENU_UZ)
# Ручная выдача курса
@dp.message_handler(commands=["send_course"])
async def admin_send_course(message: types.Message):
    admin_id = 6846748073
    if message.from_user.id == admin_id:
        await message.reply("📥 Отправляю курс...")
        await bot.send_document(chat_id=message.chat.id, document="YOUR_FILE_ID_HERE")
    else:
        await message.reply("⛔ У вас нет доступа к этой команде.")
# Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

