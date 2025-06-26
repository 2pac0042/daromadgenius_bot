from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 6846748073  # Замените на ваш Telegram ID
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# === Меню ===
LANGUAGE_KEYBOARD = types.ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGE_KEYBOARD.add("\ud83c\uddf7\ud83c\uddfa \u0420\u0443\u0441\u0441\u043a\u0438\u0439", "\ud83c\uddfa\ud83c\uddff O'zbekcha")

MENU_RU = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MENU_RU.add("\ud83d\udcca \u0418\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440\u044b", "\ud83d\udcc8 \u0421\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u0438",
           "\ud83c\udf93 \u041a\u0443\u0440\u0441\u044b", "\ud83d\udcac \u041f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430",
           "\ud83d\udce6 \u041e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0435", "\ud83d\udcb3 \u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c",
           "\ud83d\udee0 \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", "\ud83d\udcbc \u041f\u0430\u0440\u0442\u043d\u0451\u0440\u043a\u0430")

MENU_UZ = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MENU_UZ.add("\ud83d\udcca Indikatorlar", "\ud83d\udcc8 Strategiyalar",
           "\ud83c\udf93 Kurslar", "\ud83d\udcac Yordam",
           "\ud83d\udce6 Mahsulot haqida", "\ud83d\udcb3 To\u2018lov",
           "\ud83d\udee0 Sozlamalar", "\ud83d\udcbc Hamkorlik")

# === Инлайн кнопки ===
product_buttons_ru = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("\ud83d\uded2 \u041a\u0443\u043f\u0438\u0442\u044c", callback_data="buy_ru"),
    InlineKeyboardButton("\ud83d\udd19 \u041d\u0430\u0437\u0430\u0434", callback_data="back_ru")
)

product_buttons_uz = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("\ud83d\uded2 Xarid qilish", callback_data="buy_uz"),
    InlineKeyboardButton("\ud83d\udd19 Orqaga", callback_data="back_uz")
)

# === Команды ===
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("\ud83d\udc4b \u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c! / Xush kelibsiz!\n\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u044f\u0437\u044b\u043a:", reply_markup=LANGUAGE_KEYBOARD)

# Язык
@dp.message_handler(lambda m: m.text == "\ud83c\uddf7\ud83c\uddfa \u0420\u0443\u0441\u0441\u043a\u0438\u0439")
async def ru_menu(message: types.Message):
    await message.answer("\ud83c\uddf7\ud83c\uddfa \u041c\u0435\u043d\u044e:", reply_markup=MENU_RU)

@dp.message_handler(lambda m: m.text == "\ud83c\uddfa\ud83c\uddff O'zbekcha")
async def uz_menu(message: types.Message):
    await message.answer("\ud83c\uddfa\ud83c\uddff Menyu:", reply_markup=MENU_UZ)

# === Категории ===
@dp.message_handler(lambda m: m.text in ["\ud83d\udcca \u0418\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440\u044b", "\ud83d\udcca Indikatorlar"])
async def indicator(message: types.Message):
    await message.answer("\ud83d\udcca Индикатор: 25$\n\ud83d\udccc Чек отправьте: @forex0042", reply_markup=product_buttons_ru)

@dp.message_handler(lambda m: m.text in ["\ud83d\udcc8 \u0421\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u0438", "\ud83d\udcc8 Strategiyalar"])
async def strategy(message: types.Message):
    await message.answer("\ud83d\udcc8 Стратегия: 35$\n\ud83d\udccc Чек отправьте: @forex0042", reply_markup=product_buttons_ru)

@dp.message_handler(lambda m: m.text in ["\ud83c\udf93 \u041a\u0443\u0440\u0441\u044b", "\ud83c\udf93 Kurslar"])
async def course(message: types.Message):
    await message.answer("\ud83c\udf93 Курс: 290$\n\ud83d\udccc Чек отправьте: @forex0042", reply_markup=product_buttons_ru)

# === Оплата ===
@dp.message_handler(lambda m: m.text in ["\ud83d\udcb3 \u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", "\ud83d\udcb3 To\u2018lov"])
async def payment(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("\ud83d\udd17 Payme", url="https://payme.uz/example"),
        InlineKeyboardButton("\ud83d\udcc4 Копировать карту", callback_data="copy_card"),
        InlineKeyboardButton("\ud83d\udcb8 Я оплатил", callback_data="paid"),
        InlineKeyboardButton("\ud83d\udce9 Поддержка", url="https://t.me/forex0042")
    )
    await message.answer("\ud83d\udcb3 Способы оплаты:\n\nClick: +998 95 112 00 42\nPayme: нажмите кнопку ниже\nMasterCard: 5477 3300 4324 0989\n\nПосле оплаты отправьте чек: @forex0042", reply_markup=kb)

# === Inline callbacks ===
@dp.callback_query_handler(lambda c: c.data == "copy_card")
async def copy_card(callback: types.CallbackQuery):
    await callback.message.answer("\ud83d\udcb3 5477 3300 4324 0989")

@dp.callback_query_handler(lambda c: c.data == "paid")
async def paid_confirm(callback: types.CallbackQuery):
    user = callback.from_user
    log_text = f"[{datetime.now()}] {user.full_name} ({user.id}) нажал 'Оплатил'\n"
    with open("purchase_logs.txt", "a", encoding="utf-8") as f:
        f.write(log_text)
    await bot.send_message(chat_id=ADMIN_ID, text=log_text)

    # Отправка PDF курса
    if os.path.exists("Технический_анализ_для_начинающих.pdf"):
        await bot.send_document(chat_id=user.id, document=open("Технический_анализ_для_начинающих.pdf", "rb"))
        await callback.message.answer("\ud83d\udce5 Курс отправлен!")
    else:
        await callback.message.answer("❌ Файл курса не найден. Напишите @forex0042")

# === Продукт ===
@dp.message_handler(lambda m: m.text in ["\ud83d\udce6 \u041e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0435", "\ud83d\udce6 Mahsulot haqida"])
async def about(message: types.Message):
    text = ("\ud83c\udfe2 <b>Ты получаешь:</b>\n\n"
            "✅ Индикатор TradingView\n✅ Стратегия\n✅ Видеокурс\n✅ Поддержка 24/7\n\n"
            "🔥 <b>Цена раньше: 1300$</b>\n💰 <b>Сейчас: 290$</b>\n\n"
            "@daromadgeniusbot")
    await message.answer(text, parse_mode="HTML")

# === Партнёрка ===
@dp.message_handler(lambda m: m.text in ["\ud83d\udcbc \u041f\u0430\u0440\u0442\u043d\u0451\u0440\u043a\u0430", "\ud83d\udcbc Hamkorlik"])
async def partner(message: types.Message):
    await message.answer("\ud83d\ude9c Пригласи 3 друзей — получи курс бесплатно!\nСвязь: @forex0042")

# === Настройки ===
@dp.message_handler(lambda m: m.text in ["\ud83d\udee0 \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", "\ud83d\udee0 Sozlamalar"])
async def settings(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f"\u2699\ufe0f Настройки:\nВаш Telegram ID: <code>{user_id}</code>\nПоддержка: @forex0042", parse_mode="HTML")

# === Запуск ===
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
