import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choise_btn import choice, apple_keyboard
from loader import dp


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer(text="Tanlang:",
                         reply_markup=choice)

@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buy_apple(call: CallbackQuery, callback_data=dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Jami savatdagi mahsulot: {quantity}",
                              reply_markup=apple_keyboard)