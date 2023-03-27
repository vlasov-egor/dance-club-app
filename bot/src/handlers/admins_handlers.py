from aiogram import types


async def admin_start_handler(message: types.Message):
    kb = types.ReplyKeyboardMarkup(keyboard=[
        # Todo: change url
        [types.KeyboardButton(text="Сюда переходи", web_app=types.WebAppInfo(url="https://6a30-188-130-155-160.eu.ngrok.io/"))]
    ])
    await message.answer("Привет, нажми на кнопку внизу (нужно бы переделать этот текст)", reply_markup=kb)
