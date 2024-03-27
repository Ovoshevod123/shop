from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.enums import ParseMode
from first_prodject import reply

rt = Router()

@rt.message(Command('start'))
async def start(message: Message):
    await message.answer('<b>Текст1</b>, <i>Текст2</i>, <u>Текст3</u>, <s>Текст4</s>, <tg-spoiler>Текст5</tg-spoiler>, <pre>Текст6</pre>, <blockquote>Текст7</blockquote>, ', reply_markup=reply.start_kb.as_markup(resize_keyboard=True), parse_mode=ParseMode.HTML)

@rt.message(F.text.lower() == 'меню')
async def start(message: Message):
    await message.answer('menu', reply_markup=reply.start_kb2.as_markup(resize_keyboard=True))

@rt.message(F.text.lower() == 'button 2')
async def start(message: Message):
    await message.answer('opros', reply_markup=reply.start_kb2.as_markup(resize_keyboard=True))

class AddProduct(StatesGroup):
    #Шаги состояний
    name = State()
    description = State()
    price = State()
    image = State()

@rt.message(StateFilter(None), F.text == "Добавить товар")
async def add_product(message: types.Message, state: FSMContext):
    await message.answer(
        "Введите название товара", reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(AddProduct.name)
@rt.message(F.text)
async def text(message:Message):
    await message.answer('it`s text')