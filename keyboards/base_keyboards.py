from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_go_home = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Перейти',
                                                                         callback_data='new_bot',
                                                                         url='https://t.me/GGMedBot')]])
