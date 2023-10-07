from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

car_brands = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Mercedes"),
    KeyboardButton(text="BMW")],
    [KeyboardButton(text="Audi"),
    KeyboardButton(text="Toyota")]],
    resize_keyboard=True,
)

mercedes_models = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text="Geländewagen", callback_data="g-class"),
     InlineKeyboardButton(text="AMG GT", callback_data="amg")],
    [InlineKeyboardButton(text="Maybach S-class", callback_data="maybach")]
])

BMW_models = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text="X7", callback_data="x7"),
     InlineKeyboardButton(text="M8", callback_data="m8")],
    [InlineKeyboardButton(text="IX", callback_data="ix")]
])

audi_models = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text="R8", callback_data="r8"),
     InlineKeyboardButton(text="Q8", callback_data="q8")],
    [InlineKeyboardButton(text="RS7", callback_data="rs7")]
])

toyota_models = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text="Celica", callback_data="celica"),
     InlineKeyboardButton(text="Camry", callback_data="camry")],
    [InlineKeyboardButton(text="Prius", callback_data="prius")]
])

