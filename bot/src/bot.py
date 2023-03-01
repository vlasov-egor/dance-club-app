import asyncio
from aiogram import Bot, Dispatcher
from config import get_config
from handlers.admins_handlers import admin_start_handler

config = get_config()
bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


async def main():
    try:
        dp.register_message_handler(admin_start_handler, commands="start")
        await dp.start_polling()

    except Exception as e:
        # Todo: change to logging
        print("Error starting bot", e)

    finally:
        session = await bot.get_session()
        await session.close()


if __name__ == "__main__":
    asyncio.run(main())
