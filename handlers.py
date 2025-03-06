from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router



router = Router()

@router.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer("Привет! Спроси меня что-нибудь")

@router.message(Command(commands=['help']))
async def process_start_command(message: Message):
    await message.answer("Выбери нужное действие")

@router.message(Command(commands=['weather']))
async def process_start_command(message: Message):
    await message.answer("Погода на сегодня")

@router.message(Command(commands=['courses']))
async def process_start_command(message: Message):
    await message.answer("Курс доллара и евро на сегодня")

@router.message(Command(commands=['vacancies']))
async def process_start_command(message: Message):
    await message.answer("Три случайные вакансии Python-разработчика")