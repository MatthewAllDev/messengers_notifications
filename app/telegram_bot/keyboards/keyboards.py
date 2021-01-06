from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

send_phone_number: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Send my phone number ☎️', request_contact=True))
