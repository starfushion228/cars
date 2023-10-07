import asyncio
import sys
from os import getenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import keyboards as kb
import const

dp = Dispatcher()


@dp.message(F.text == "/start")
async def command_start(message: Message):
    await message.answer("Привіт! Щоб користуватися ботом використовуйте кнопки знизу ", reply_markup=kb.car_brands)

@dp.message(F.text == "Mercedes")
async def command_mercedes(message: Message):
    await message.answer_photo(photo=const.MERCEDES_LOGO_URL,
                               reply_markup=kb.mercedes_models)
@dp.callback_query(F.data == "g-class")
async def command_mercedes_g(callback: CallbackQuery):
    await callback.message.answer_photo(photo=const.MERCEDES_G_PHOTO, 
                                        caption=const.MERCEDES_G_CAPTION)
@dp.callback_query(F.data == "amg")
async def command_mercedes_amg(callback: CallbackQuery):
    await callback.message.answer_photo(photo=const.MERCEDES_AMG_PHOTO,
                                        caption=const.MERCEDES_AMG_CAPTION)
@dp.callback_query(F.data == "maybach")
async def command_mercedes_maybach(callback: CallbackQuery):
    await callback.message.answer_photo(photo=const.MERCEDES_MAYBACH_PHOTO,
                                        caption=const.MERCEDES_MAYBACH_CAPTION)

@dp.message(F.text == "BMW")
async def command_BMW(message: Message):
    await message.answer_photo(photo=const.BMW_LOGO_URL,
                               reply_markup=kb.BMW_models)
@dp.callback_query(F.data == "x7")
async def command_BMW_x7(callback: CallbackQuery):
    await callback.message.answer_photo(photo=const.BMW_X7_PHOTO,
                                        caption=const.BMW_X7_CAPTION)
@dp.callback_query(F.data == "m8")
async def command_BMW_m8(callback: CallbackQuery):
    await callback.message.answer_photo(photo=const.BMW_M8_PHOTO,
                                        caption=const.BMW_M8_CAPTION)
@dp.callback_query(F.data == "ix")
async def command_BMW_ix(callback: CallbackQuery):
    await callback.message.answer_photo(photo=const.BMW_IX_PHOTO,
                                        caption=const.BMW_IX_CAPTION)

@dp.message(F.text == "Audi")
async def command_audi(message: Message):
    await message.answer_photo(photo=const.AUDI_LOGO_URL,
                               reply_markup=kb.audi_models)
@dp.callback_query(F.data == "r8")
async def command_audi_r8(callback: CallbackQuery):
    await callback.message.answer_photo(photo=const.AUDI_R8_PHOTO,
                               caption=const.AUDI_R8_CAPTION)
@dp.callback_query(F.data == "q8")
async def command_audi_q8(callback: CallbackQuery):
    await callback.message.answer_photo(photo=const.AUDI_Q8_PHOTO,
                               caption=const.AUDI_Q8_CAPTION)
@dp.callback_query(F.data == "rs7")
async def command_audi_rs7(callback: CallbackQuery):
    await callback.message.answer_photo(photo=const.AUDI_RS7_PHOTO,
                               caption=const.AUDI_RS7_CAPTION)

@dp.message(F.text == "Toyota")
async def command_toyota(message: Message):
    await message.answer_photo(photo=const.TOYOTA_LOGO_URL,
                               reply_markup=kb.toyota_models)
@dp.callback_query(F.data == "celica")
async def command_toyota_celica(callback: CallbackQuery):
    await callback.message.answer_photo(photo=const.TOYOTA_CELICA_PHOTO,
                               caption=const.TOYOTA_CELICA_CAPTION)
@dp.callback_query(F.data == "camry")
async def command_toyota_camry(callback: CallbackQuery):
    await callback.message.answer_photo(photo=const.TOYOTA_CAMRY_PHOTO,
                               caption=const.TOYOTA_CAMRY_CAPTION)
@dp.callback_query(F.data == "prius")
async def command_toyota_prius(callback: CallbackQuery):
    await callback.message.answer_photo(photo=const.TOYOTA_PRIUS_PHOTO,
                               caption = const.TOYOTA_PRIUS_CAPTION)




@dp.message()
async def echo_handler(message: Message):
    await message.answer("Будь ласка використайте кнопки телеграмма.")


async def main():
    bot = Bot(const.TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
