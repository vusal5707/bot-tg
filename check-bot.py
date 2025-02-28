import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

TOKEN = "7717469656:AAH-ECdtNeqzNGmBIAuEaUFhPTQeE-Liq7M"
DOMAIN = "https://sanslisaray674.com"  # Замените на нужный домен
CHECK_INTERVAL = 900  # 15 минут (в секундах)
YOUR_TELEGRAM_USER_ID = "7803376405"  # Замените на ваш Telegram ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

async def check_domain():
    while True:
        try:
            response = requests.get(DOMAIN, timeout=5)
            if response.status_code == 200:
                status = "✅ Домен доступен"
            else:
                status = f"⚠️ Проблема с доменом, код ответа: {response.status_code}"
        except requests.exceptions.RequestException:
            status = "❌ Домен недоступен!"
        
        await bot.send_message(YOUR_TELEGRAM_USER_ID, status)
        await asyncio.sleep(CHECK_INTERVAL)

@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    await message.answer("Привет! Я буду проверять статус домена каждые 15 минут.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(check_domain())
    executor.start_polling(dp, skip_updates=True)
