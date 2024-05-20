from aiogram.types import Message
from aiogram import F, Router
from aiogram.filters import CommandStart, Command

router = Router()

@router.message(CommandStart())
async def say_hello(message: Message):
    await message.reply("Hello! Nice to meet you!")
    await message.answer("How can I help you?")


@router.message()
async def reply_to_messages(message:Message):
    await message.reply("I don't understand you. Try again")