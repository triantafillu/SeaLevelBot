from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Add inline buttons ("algorithm" and "prediction")
inline_btn_1 = InlineKeyboardButton('Algorithm', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Prediction', callback_data='button2')
inline_kb = InlineKeyboardMarkup().add(inline_btn_2, inline_btn_1)