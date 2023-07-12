from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callback.animals import AnimalsCallback

cats = InlineKeyboardButton(text='Коты', callback_data=AnimalsCallback(animal='Кот', count=4).pack())
dogs = InlineKeyboardButton(text='Собаки', callback_data=AnimalsCallback(animal='Собака', count=5).pack())
fish = InlineKeyboardButton(text='Рыбы', callback_data=AnimalsCallback(animal='Рыба', count=1).pack())
owl = InlineKeyboardButton(text='Совы', callback_data=AnimalsCallback(animal='Сова', count=10).pack())

cats_dogs_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [cats, dogs],
    [fish, owl]
])
