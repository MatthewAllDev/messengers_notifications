import logging
import os

tg_token: str = ''
db_path: str = 'database.db'

# logging settings
if not os.path.exists('log'):
    os.mkdir('log')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
full: logging.Handler = logging.FileHandler('log/full.log')
full.setLevel(logging.INFO)
errors: logging.Handler = logging.FileHandler('log/errors.log')
errors.setLevel(logging.ERROR)
handlers = [console, full, errors]
# noinspection PyArgumentList
logging.basicConfig(format='%(asctime)s - %(levelname)s:%(name)s:%(message)s',
                    level=logging.INFO,
                    datefmt='%d.%m.%y %H:%M:%S',
                    handlers=handlers)
