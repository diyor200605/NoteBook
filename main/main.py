from aiogram.types import Message
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext


dp = Dispatcher()
router = Router()

token='8216319063:AAHu6gCuUl4UFB1WW_E3TTiKv8F6o4zqxTg'
bot = Bot(token=token)



async def main():
    init_db()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    dp.include_router(router)
    dp.run_polling(bot)