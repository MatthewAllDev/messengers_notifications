from multiprocessing import Process
from telegram_bot import bot
from rest_api_server import server

server_proc: Process = Process(target=server.run, name='messengers_notifications_api_server')
tg_bot_proc: Process = Process(target=bot.start_polling, name='telegram_bot')
server_proc.start()
tg_bot_proc.start()

server_proc.join()
tg_bot_proc.join()
