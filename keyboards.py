from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def simple_keyboard():
    btn_1 = KeyboardButton(text="Кнопка 1")
    btn_2 = KeyboardButton(text="Кнопка 2")

    keybord = ReplyKeyboardMarkup(resize_keyboard=True,
                                  one_time_keyboard=True,
                                  keyboard=[[btn_1, btn_2]])
    return keybord

