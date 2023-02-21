import asyncio
from aiogram import Bot
from config import get_config

config = get_config()


async def main():
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)

    try:
        me = await bot.get_me()
        print(f"🤖 Hello, I'm {me.first_name}.\nHave a nice Day!")
    finally:
        session = await bot.get_session()
        await session.close()


asyncio.run(main())
