from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio






# Создание инлайн-кнопок и клавиатур
inline_btn_help = InlineKeyboardButton(text='💻 Наш сайт', callback_data='sait')
inline_btn_assortment = InlineKeyboardButton(text='🪑 Ассортимент', callback_data='assortment')
inline_btn_reviews = InlineKeyboardButton(text='Отзывы!', callback_data='reviews')
inline_kb1 = InlineKeyboardMarkup(inline_keyboard=[[inline_btn_assortment, inline_btn_help], [inline_btn_reviews]])

# Кнопки полного ассортимента
button_himich_mebel = InlineKeyboardButton(text='🔬 Мебель на производство', callback_data='himich_mebel')
button_ofice_mebel = InlineKeyboardButton(text='💼 Офисная мебель', callback_data='ofice_mebel')
button_solo_zakaz = InlineKeyboardButton(text='🫵 Индивидуальный заказ', callback_data='solo_zakaz')
button_back = InlineKeyboardButton(text='🔙 Назад', callback_data='back')
assortment_kb = InlineKeyboardMarkup(inline_keyboard=[[button_himich_mebel], [button_ofice_mebel,] , [button_solo_zakaz,] , [button_back]])


inline_btn_podrobnee1 = InlineKeyboardButton(text='Подробнее', url='https://tornadolab.ru')
inline_podrobnee = InlineKeyboardMarkup(inline_keyboard=[[inline_btn_podrobnee1] , [button_back]])


#кнопки для ассортимента офисной мебели
button_stol = InlineKeyboardButton(text='🗃 Cтолы', callback_data='himich_stol')
button_stul = InlineKeyboardButton(text='🪑 Стулья', callback_data='ofice_stul')
button_skkafi = InlineKeyboardButton(text='🗄 Шкафы и тумбочки', callback_data='skafi')
button_back2 = InlineKeyboardButton(text='🔙 Назад', callback_data='back2')
assortment_office_mebel = InlineKeyboardMarkup(inline_keyboard=[[button_stol, button_stul] , [button_skkafi,] , [button_back2]])

button_keybord_news = KeyboardButton(text="🗞 Новости")
button_keybord_korzina = KeyboardButton(text="🗑 Корзина")
button_keybord_otzv = KeyboardButton(text="🏠 Меню")
button_keybord_zakaz = KeyboardButton(text="🛒 Заказы")
button_keybord_help = KeyboardButton(text="🆘 Поддержка")
button_keybord_contacts = KeyboardButton(text="☎️ Контакты")
knopki_key = ReplyKeyboardMarkup(keyboard=[[button_keybord_news , button_keybord_help] , [button_keybord_contacts, button_keybord_zakaz] , [button_keybord_korzina , button_keybord_otzv]], resize_keyboard= True)



