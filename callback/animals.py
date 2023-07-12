from aiogram.filters.callback_data import CallbackData


class AnimalsCallback(CallbackData, prefix='animals'):
    animal: str
    count: int

