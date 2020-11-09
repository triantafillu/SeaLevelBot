import asyncio
import os
import logging
from urllib.parse import urljoin
from aiogram import Bot, Dispatcher
from aiogram.types import ContentTypes
from aiogram.utils.executor import start_webhook
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '1463776929:AAF9xdulEOKucqjWjYzseWF3qyAIGkNr_ok'
PROJECT_NAME = 'young-citadel-27894'

WEBHOOK_HOST = f'https://{PROJECT_NAME}.herokuapp.com/'
WEBHOOK_URL_PATH = '/webhook/' + TOKEN
WEBHOOK_URL = urljoin(WEBHOOK_HOST, WEBHOOK_URL_PATH)

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.environ.get('PORT')

BAD_CONTENT = ContentTypes.PHOTO & ContentTypes.DOCUMENT & ContentTypes.STICKER & ContentTypes.AUDIO

loop = asyncio.get_event_loop()
bot = Bot(token=TOKEN, parse_mode = "markdownv2")
storage = MemoryStorage()
dp = Dispatcher(bot)
logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    logging.info(dp)

async def on_shutdown(dp):
    logging.info(dp)

if __name__ == '__main__':
    from handlers import dp
    start_webhook(dispatcher=dp, webhook_path=WEBHOOK_URL_PATH,
                  on_startup=on_startup, on_shutdown=on_shutdown,
                  host=WEBAPP_HOST, port=WEBAPP_PORT)