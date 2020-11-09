from bot import bot, dp
import logging
from aiogram import types
from aiogram.types.message import ContentType
from aiogram.types import CallbackQuery

import keyboards as kb
import sea_level_predictor as slp
from messages import *
import os

#/start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(start_message)

#/help
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)

#/references
@dp.message_handler(commands=['references'])
async def process_help_command(message: types.Message):
    await message.reply(references_message)

#/menu
@dp.message_handler(commands=['menu'])
async def process_command_1(message: types.Message):
    await message.reply(menu_message, reply_markup=kb.inline_kb)

#Handler of the "Algorithm" button
@dp.callback_query_handler(text_contains="button1")
async def alg_handler(call: CallbackQuery):
    #hide the "clock"
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer(algorithm_message)

#Handler of the "Prediction" button
@dp.callback_query_handler(text="button2")
async def pred_handler(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")
    await call.message.reply(prediction_message)

#Handler of the text messages
@dp.message_handler()
async def year_func(ms: types.Message):
    #Check whether the message is a number
    if(ms.text.isnumeric()):
        #Check whether a number starts with 0
        if(int(ms.text[:1])==0):
            await ms.reply(starts_with_zero_message)
        #Check whether the number is less than 1880
        elif(int(ms.text)<1880):
            await ms.reply(less_than_message)
        # Check whether the number is valis as a year
        elif (int(ms.text)>=1880):
            #Generate the plot
            level = slp.draw_plot(int(ms.text))
            caption_message = text("Here is your plot\!",
                                   f"\nThe sea level for a chosen year is {level} inches \(compared to the sea level in 1880\)\.",
                                   emojize("\n\n:droplet:  :droplet:  :droplet:"))

            #Open the file with plot
            f = open("sea_level_plot.png", "rb")

            #Send the plot with caption
            await bot.send_photo(chat_id=ms.from_user.id, photo=f, caption=caption_message,
                                 reply_to_message_id=ms.message_id)

            #Close the file
            f.close()

            #Delete the file
            os.unlink("sea_level_plot.png")
    else:
        await ms.reply(notnumeric_message)

#Handler of any other type of messages (not text)
@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text(emojize("Sorry, the bot can't understand this:astonished:"),
                        "\nYou can use ", italic("/help"), " to see available commands")
    await msg.reply(message_text)

