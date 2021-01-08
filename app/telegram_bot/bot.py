import settings
from aiogram import Bot as TgBot, Dispatcher, executor
from db import User


class Bot:
    dispatcher: Dispatcher

    def __init__(self):
        self.bot: TgBot = TgBot(settings.tg_token)
        self.dispatcher: Dispatcher = Dispatcher(self.bot)

    def start_polling(self):
        executor.start_polling(self.dispatcher, skip_updates=True)

    async def send_message_to_phone_number(self, phone_number: str, text: str) -> dict:
        user: User = User(phone_number)
        user: User = user.get()
        if user is not None:
            await self.bot.send_message(user.tg_user_id, text, parse_mode='html')
            return {'success': 'Message sent'}
        else:
            return {'error': 'Recipient not found'}
