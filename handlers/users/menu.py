from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Tavorni menudan tanlang", reply_markup=menu)

@dp.message_handler(text="samsung")
async def samsung(message: types.Message):
    await message.answer("Samsungni tanladingiz!")

@dp.message_handler(Text(equals=["dell", "acer"]))
async def two_brand(message: types.Message):
    brand = message.text
    await message.answer(f"{brand}ni tanladingiz!", reply_markup=ReplyKeyboardRemove())
