from aiogram import types


async def admin_start_handler(message: types.Message):
    kb = types.ReplyKeyboardMarkup(keyboard=[
        # Todo: change url
        [types.KeyboardButton(text="Сюда переходи", web_app=types.WebAppInfo(url="https://google.com/"))]
    ])
    await message.answer("Привет, нажми на кнопку внизу (нужно бы переделать этот текст)", reply_markup=kb)
