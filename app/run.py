from multiprocessing import Process

from rest_api_server import server
from telegram_bot import bot

server_proc: Process = Process(target=server.run, name='messengers_notifications_api_server')
tg_bot_proc: Process = Process(target=bot.start_polling, name='telegram_bot')
server_proc.start()
tg_bot_proc.start()

server_proc.join()
tg_bot_proc.join()
