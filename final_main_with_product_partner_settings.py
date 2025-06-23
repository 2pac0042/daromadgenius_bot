# ... (весь предыдущий код выше остаётся без изменений)

# 📦 О ПРОДУКТЕ
@dp.message_handler(lambda m: m.text in ["📦 О продукте", "📦 Mahsulot haqida"])
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
    text_uz = (
        "📦 Бу шунчаки курс эмас. Бу 🔥 тўлиқ тўплам:

"
        "✔️ Кириш учун аниқ индикатор
"
        "✔️ Бозорда синаб кўрилган стратегиялар
"
        "✔️ Профессионаллардан видео дарслар
"
        "✔️ Доимий ёрдам

"
        "💥 Ҳаммаси — 1300$ эмас, фақат 👉 290$
"
        "🚀 Фақат танланганлар учун. Шошилинг!"
    )
    if message.text == "📦 О продукте":
        await message.answer(text_ru)
    else:
        await message.answer(text_uz)

# 💼 ПАРТНЁРКА
@dp.message_handler(lambda m: m.text in ["💼 Партнёрка", "💼 Hamkorlik"])
async def partnership(message: types.Message):
    text_ru = (
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
    text_uz = (
        "💼 Ҳамкорлик дастури:

"
        "👥 Дўстлар ва трейдерларни таклиф этинг
"
        "💰 Ҳар бир буюртмадан 20% олинг
"
        "📩 Уланиш учун: @forex0042

"
        "⚠️ Фақат фаоллар учун!"
    )
    if message.text == "💼 Партнёрка":
        await message.answer(text_ru)
    else:
        await message.answer(text_uz)

# ⚙️ НАСТРОЙКИ
@dp.message_handler(lambda m: m.text in ["🛠 Настройки", "🛠 Sozlamalar"])
async def settings(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
        InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data="lang_uz")
    )
    await message.answer("🌐 Выберите язык / Tilni tanlang:", reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data.startswith("lang_"))
async def change_language(callback: types.CallbackQuery):
    lang = "Русский" if callback.data.endswith("ru") else "O'zbekcha"
    await callback.message.answer(f"✅ Язык изменён на: {lang}")