from aiogram.types import Message
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from database import init_db, add_mentions, del_mentions, get_mentions


dp = Dispatcher()
router = Router()

token='8216319063:AAHu6gCuUl4UFB1WW_E3TTiKv8F6o4zqxTg'
bot = Bot(token=token)


@router.message(CommandStart())
async def cmd_str(message: Message):
    await message.answer("👋 Привет! Я твоя записная книжка в Telegram.\n\n"
        "Доступные команды:\n"
        "/add — добавить заметку\n"
        "/list — показать все заметки\n"
        "/delete — удалить заметку по тексту\n")


@router.message(Command('add'))
async def cmd_add(message: Message):
    add_mentions(message.from_user.id, message.text)
    await message.answer('Твоя Заметка добавлена✅!')

@router.message(Command('list'))
async def cmd_list(message: Message):
    notes = get_mentions(message.from_user.id)
    if not notes:
        await message.answer('У вас нет заметок🤷!')
    else:


@router.message(Command('del'))
async def cmd_del(message: Message):
    del_mentions(message.from_user.id,message.text)
    await message.answer("Заметка удалена🗑!")





async def main():
    init_db()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    dp.include_router(router)
    dp.run_polling(bot)