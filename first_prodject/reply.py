from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardBuilder()
start_kb.add(
    KeyboardButton(text='меню'),
    KeyboardButton(text='Добавить товар')
)
start_kb.adjust(2)

start_kb2 = ReplyKeyboardBuilder()
start_kb2.attach(start_kb)
start_kb2.row(KeyboardButton(text='Button 3'))

del_kb = ReplyKeyboardRemove()