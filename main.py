import asyncio
from aiogram import Bot, Dispatcher

from apps.hendlers import router


async def main():
    bot = Bot(token='6879245989:AAF0M5BiygRCCRK0OQhU1x8dKD3klWSw_WM')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stop working!")
        
         