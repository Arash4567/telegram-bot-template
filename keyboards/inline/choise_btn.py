from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Buy apple",
                                          callback_data=buy_callback.new(item_name="apple",
                                                                         quantity=5)
                                      ),
                                      InlineKeyboardButton(
                                          text="Buy poco",
                                          callback_data="buy:poco:3"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Bekor qilish",
                                          callback_data="cancel"
                                      )
                                  ]
                              ])
apple_keyboard = InlineKeyboardMarkup()

APPLE_LINK = "https://apple.com"

apple_link = InlineKeyboardButton(text="Buy now", url=APPLE_LINK)

apple_keyboard.insert(apple_link)