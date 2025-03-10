from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

from api.courses_api import get_courses
from api.weather_api import get_weather
from api.vacancies_api import get_vacancies


router = Router()

@router.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer("Привет! Спроси меня что-нибудь")

@router.message(Command(commands=['help']))
async def process_start_command(message: Message):
    await message.answer("Выбери нужное действие")

@router.message(Command(commands=['weather']))
async def process_start_command(message: Message):
    weather = get_weather()
    await message.answer("Погода на сегодня")

@router.message(Command(commands=['courses']))
async def process_start_command(message: Message):
    courses = get_courses()
    await message.answer("Курс доллара и евро на сегодня")

@router.message(Command(commands=['vacancies']))
async def process_start_command(message: Message):
    vacancies = get_vacancies()
    await message.answer("Три случайные вакансии Python-разработчика")
    await message.answer("Три случайные вакансии Python-разработчика")
    await message.answer("Три случайные вакансии Python-разработчика")