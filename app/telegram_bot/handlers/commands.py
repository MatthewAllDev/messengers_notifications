from aiogram import types
from db import User
from telegram_bot import bot

from ..keyboards import send_phone_number


@bot.dispatcher.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\n"
                        "To continue working, please submit your phone number by clicking on the button below.\n",
                        reply_markup=send_phone_number)


@bot.dispatcher.message_handler(content_types=types.ContentTypes.CONTACT)
async def save_contact(message: types.Message):
    if message.from_user.id == message.contact.user_id:
        await message.reply('Thank you! I remembered you', reply_markup=types.ReplyKeyboardRemove())
        user: User = User(message.contact.phone_number, message.contact.user_id, message.contact.first_name)
        user.save()
    else:
        await message.reply('No, no, no...\nYou can\'t fool me!')
