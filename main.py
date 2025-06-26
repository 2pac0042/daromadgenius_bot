from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import logging
import os

API_TOKEN = os.getenv("7481276211:AAFtUF5vKB4PFYiXZq1wYvOqhq61ox2xVoM")
if not API_TOKEN:
    raise ValueError("❌ BOT_TOKEN не установлен в переменных окружения Railway")

ADMIN_ID = 6846748073  # Замените на ваш Telegram ID
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

LANGUAGE_KEYBOARD = types.ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGE_KEYBOARD.add("\ud83c\uddf7\ud83c\uddfa Русский", "\ud83c\uddfa\ud83c\uddff O'zbekcha")

MENU_RU = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MENU_RU.add(
    "\ud83d\udcca Индикаторы", "\ud83d\udcc8 Стратегии",
    "\ud83c\udf93 Курсы", "\ud83d\udcac Поддержка",
    "\ud83d\udce6 О продукте", "\ud83d\udcb3 Оплатить",
    "\ud83d\udee0 Настройки", "\ud83d\udcbc Партнёрка"
)

MENU_UZ = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
MENU_UZ.add(
    "\ud83d\udcca Indikatorlar", "\ud83d\udcc8 Strategiyalar",
    "\ud83c\udf93 Kurslar", "\ud83d\udcac Yordam",
    "\ud83d\udce6 Mahsulot haqida", "\ud83d\udcb3 To\u2018lov",
    "\ud83d\udee0 Sozlamalar", "\ud83d\udcbc Hamkorlik"
)

product_buttons_ru = InlineKeyboardMarkup(row_width=2)
product_buttons_ru.add(
    InlineKeyboardButton("\ud83d\uded2 Купить", callback_data="buy_ru"),
    InlineKeyboardButton("\ud83d\udd19 Назад", callback_data="back_ru")
)

product_buttons_uz = InlineKeyboardMarkup(row_width=2)
product_buttons_uz.add(
    InlineKeyboardButton("\ud83d\uded2 Xarid qilish", callback_data="buy_uz"),
    InlineKeyboardButton("\ud83d\udd19 Orqaga", callback_data="back_uz")
)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("\ud83d\udc4b Добро пожаловать! / Xush kelibsiz!\nВыберите язык:", reply_markup=LANGUAGE_KEYBOARD)

@dp.message_handler(lambda m: m.text == "\ud83c\uddf7\ud83c\uddfa Русский")
async def ru_menu(message: types.Message):
    await message.answer("\ud83c\uddf7\ud83c\uddfa Меню:", reply_markup=MENU_RU)

@dp.message_handler(lambda m: m.text == "\ud83c\uddfa\ud83c\uddff O'zbekcha")
async def uz_menu(message: types.Message):
    await message.answer("\ud83c\uddfa\ud83c\uddff Menyu:", reply_markup=MENU_UZ)

@dp.message_handler(lambda m: m.text in ["\ud83d\udcca Индикаторы", "\ud83d\udcca Indikatorlar"])
async def indicators(message: types.Message):
    await message.answer("\ud83d\udcca Индикатор: 25$/250,000 so'm\n\ud83d\udccc Чек: @forex0042", reply_markup=product_buttons_ru if message.text.startswith("\ud83c\uddf7") else product_buttons_uz)

@dp.message_handler(lambda m: m.text in ["\ud83d\udcc8 Стратегии", "\ud83d\udcc8 Strategiyalar"])
async def strategies(message: types.Message):
    await message.answer("\ud83d\udcc8 Стратегия: 35$/350,000 so'm\n\ud83d\udccc Чек: @forex0042", reply_markup=product_buttons_ru if message.text.startswith("\ud83c\uddf7") else product_buttons_uz)

@dp.message_handler(lambda m: m.text in ["\ud83c\udf93 Курсы", "\ud83c\udf93 Kurslar"])
async def courses(message: types.Message):
    await message.answer("\ud83c\udf93 Курс: 290$/3 100 000 so'm\n\ud83d\udccc Чек: @forex0042", reply_markup=product_buttons_ru if message.text.startswith("\ud83c\uddf7") else product_buttons_uz)

@dp.callback_query_handler(lambda c: c.data.startswith("buy_"))
async def buy(callback: types.CallbackQuery):
    await pay_ru(callback.message) if callback.data == "buy_ru" else await pay_uz(callback.message)

@dp.callback_query_handler(lambda c: c.data.startswith("back_"))
async def back(callback: types.CallbackQuery):
    await callback.message.answer("\ud83d\udd19 Главное меню:", reply_markup=MENU_RU if callback.data == "back_ru" else MENU_UZ)

@dp.message_handler(lambda m: m.text in ["\ud83d\udcb3 Оплатить", "\ud83d\udcb3 To\u2018lov"])
async def pay(message: types.Message):
    lang = "ru" if message.text.startswith("\ud83c\uddf7") else "uz"
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("\ud83d\udd17 Payme", url="https://payme.uz/example"),
        InlineKeyboardButton("\ud83d\udccb Копировать карту" if lang == "ru" else "\ud83d\udccb Kartani nusxalash", callback_data=f"copy_card_{lang}"),
        InlineKeyboardButton("\ud83d\udcb8 Я оплатил" if lang == "ru" else "\ud83d\udcb8 To\u2018lov qilindi", callback_data=f"paid_{lang}"),
        InlineKeyboardButton("\ud83d\udce9 Поддержка" if lang == "ru" else "\ud83d\udce9 Yordam", url="https://t.me/forex0042")
    )
    card_info = "\n\ud83d\udcb3 MasterCard (Anor Bank):\n`5477 3300 4324 0989`\nИмя: Anor Bank"
    await message.answer(
        f"\ud83d\udcb3 Способы оплаты:\n\n\ud83c\uddfa\ud83c\uddff Click: +998 95 112 00 42\n\ud83c\udf10 Payme: нажмите кнопку ниже{card_info}\n\n\u2705 После оплаты отправьте чек: @forex0042",
        reply_markup=kb, parse_mode="Markdown")

@dp.callback_query_handler(lambda c: c.data.startswith("copy_card"))
async def copy_card(callback: types.CallbackQuery):
    await callback.message.answer("\ud83d\udcb3 5477 3300 4324 0989")

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
    await callback.message.answer("\ud83d\udce9 Спасибо! Чек отправьте в @forex0042 для подтверждения.")

@dp.message_handler(lambda m: m.text in ["\ud83d\udce6 О продукте", "\ud83d\udce6 Mahsulot haqida"])
async def about_product(message: types.Message):
    await message.answer(
        "\ud83d\udcbc <b>Что ты получаешь:</b>\n\n\u2705 Индикатор\n\u2705 Стратегия\n\u2705 Видео-курс\n\u2705 Поддержка 24/7\n\n\ud83d\udd25 <b>Ранее: 1300$</b>\n\ud83d\udcb0 <b>Сейчас: 290$</b>\n\n\ud83d\ude80 Доступ: @daromadgeniusbot",
        parse_mode="HTML")

@dp.message_handler(lambda m: m.text in ["\ud83d\udcbc Партнёрка", "\ud83d\udcbc Hamkorlik"])
async def partner(message: types.Message):
    await message.answer(
        "\ud83e\udd1d <b>Партнёрка:</b>\n\n\ud83c\udf81 Пригласи 3 друзей — получи индикатор бесплатно\n\ud83d\udd17 Реферальная ссылка (скоро)\n\ud83d\udce9 Связь: @forex0042",
        parse_mode="HTML")

@dp.message_handler(lambda m: m.text in ["\ud83d\udee0 Настройки", "\ud83d\udee0 Sozlamalar"])
async def settings(message: types.Message):
    await message.answer(
        f"\u2699\ufe0f <b>Настройки</b>\n\n\ud83c\udf10 Язык: Русский/Uzbek\n\ud83d\udcc1 Версия: 1.0\n\ud83d\udcc6 Дата: {datetime.now().strftime('%Y-%m-%d')}\n\ud83d\udc64 ID: <code>{message.from_user.id}</code>",
        parse_mode="HTML")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

