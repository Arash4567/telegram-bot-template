from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="samsung")
        ],
        [
            KeyboardButton(text="dell"),
            KeyboardButton(text="acer"),
        ]
    ],
    resize_keyboard=True
)