import io
from string import capwords

from PIL import Image

import img
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from keybords import *
import asyncio


from database import Database


TOKEN = "7295513375:AAGO3kyVVARa2tjlixWPDxYM_4sae8HJogI"  # Замените на токен вашего бота
bot = Bot(token=TOKEN)
dp = Dispatcher()
db = Database()


photo_url = "https://mebeloptovik.ru/wp-content/uploads/2023/06/img-tornadolab.png"




@dp.message(Command(commands=["start"]))
async def send_welcome(message: types.Message):
    # Добавляем пользователя в БД
    db.add_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        full_name=message.from_user.full_name
    )

    await message.answer("🏠 Меню", reply_markup=knopki_key)
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption="🤖 Этот бот поможет разобраться в нашем магазине!\n\n✅ Совершая любое действия в боте вы соглашаетесь с правилами нашего проекта \n\n❤️ Приятного использования!",
        reply_markup=inline_kb1
    )


    @dp.message(F.text == "🗞 Заказы")
    async def handle_news(message: types.Message):
        await message.answer("📰 Новости вы можете посмотреть в нашем телеграм канале\n\🤳 @news_tornadolab")

    @dp.message(F.text == "🆘 Поддержка")
    async def handle_help(message: types.Message):
        await message.answer("📩 Напишите нам в поддержку\n📱 @support_dmitriy_bub")



@dp.message(F.text == "🏠 Меню")
async def handle_reviews(message: types.Message):
    await message.answer("🏠 Меню", reply_markup=knopki_key)
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption="🤖 Этот бот поможет разобраться в нашем магазине!\n\n✅ Совершая любое действия в боте вы соглашаетесь с правилами нашего проекта \n\n❤️ Приятного использования!",
        reply_markup=inline_kb1  # Прикрепляем инлайн-клавиатуру
    )


@dp.message(F.text == "🆘 Поддержка")
async def handle_help(message: types.Message):
    await message.answer("📩 Напишите нам в поддержку\n📱 @support_dmitriy_bub")

@dp.message(F.text == "☎️ Контакты")
async def handle_contacts(message: types.Message):
    await message.answer("📨 Вы можете написать нам в telegram или позвонить по номеру телефона\n\n Директор отдела офисной мебели Дмитрий Владимирович\n📲 @Dmitry_Bub \n\nМенеджер по продажам Булат Ильдусович\n🇷🇺 +79872695433.")


@dp.callback_query(F.data.in_(["sait", "reviews", "assortment"]))
async def handle_buttons(callback_query: types.CallbackQuery):
    if callback_query.data == 'sait':
        new_caption = "Вы можете посетить наш сайт и посмтреть наши работы а так же увидеть ассортимент и там"
        await bot.edit_message_media(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            media=InputMediaPhoto(media=photo_url),
            reply_markup=inline_podrobnee  # Сохранение инлайн-клавиатуры
        )
    elif callback_query.data == 'reviews':
        await callback_query.answer("Вы нажали кнопку 'Отзывы'.")
    elif callback_query.data == 'assortment':
        await callback_query.answer("Вы нажали кнопку 'Ассортимент'.")
        new_caption = ("Привет это новый текст")
        await bot.edit_message_media(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            media=InputMediaPhoto(media=photo_url, caption=new_caption),
            reply_markup=assortment_kb  # Сохранение инлайн-клавиатуры
        )
@dp.callback_query(F.data.in_(["solo_zakaz", "himich_mebel", "ofice_mebel", "back" , "back2"]))
async def handle_assortment_options(callback_query: types.CallbackQuery):
    if callback_query.data == 'ofice_mebel':
        await bot.edit_message_media(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            media=InputMediaPhoto(media=photo_url),
            reply_markup=assortment_office_mebel # Сохранение инлайн-клавиатуры
        )
        await callback_query.answer()
    elif callback_query.data == 'himich_mebel':
        await bot.edit_message_media(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            media=InputMediaPhoto(media=photo_url),
            reply_markup=assortment_kb  # Сохранение инлайн-клавиатуры
        )
        await callback_query.answer()
    elif callback_query.data == 'back':
        new_caption = ("🤖 Этот бот поможет разобраться в нашем магазине!\n\n✅ Совершая любое действия в боте вы соглашаетесь с правилами нашего проекта \n\n❤️ Приятного использования!")
        await bot.edit_message_media(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            media=InputMediaPhoto(media=photo_url,caption=new_caption),
            reply_markup=inline_kb1

        )
        await callback_query.answer()
    elif callback_query.data == 'back2':
        await bot.edit_message_media(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            media=InputMediaPhoto(media=photo_url),
            reply_markup=assortment_kb
        )


        await callback_query.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())