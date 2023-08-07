from django.shortcuts import render
from django.conf import settings
from aiogram import Bot, Dispatcher, types, executor
from asgiref.sync import sync_to_async
from logging import basicConfig, INFO

from apps.telegram.models import TelegramUser
from apps.posts.models import Post

# Create your views here.
bot = Bot(settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
basicConfig(level=INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    user = await sync_to_async(TelegramUser.objects.get_or_create)(
        username=message.from_user.username,
        user_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    await message.answer(f"Привет {message.from_user.full_name}")

async def send_post_message(user:str, title:str, description:str):
    await bot.send_message(731982105, f"Новый пост на сайте\nЗаголовок: {title}\nОписание: {description}\nПользователь {user}")