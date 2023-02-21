from aiogram import types


async def admin_start_handler(message: types.Message):
    await message.reply("Hi, dear customer")
