import asyncio
import random
import os
import time
import requests
from random import  choice, randint
from pyrogram import Client, filters
from FallenMusic.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from FallenMusic import app


@app.on_message(
    command(["سورس","السورس","المطور"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6fe7de7485c993122bc4a.jpg",
        caption=f"""Developer Name : hamody . 
Devloper Username : @MH_BP ، 
‏ⓘ متسالنيش عن احوالي انا تايه .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " مطور السورس .", url=f"https://t.me/MH_BP"),
                ],
                [
                   InlineKeyboardButton(
                        "𓏺 ََِ𝗠𝗔𝗗𝗥𝗜𝗗 ↺", url=f"https://t.me/M_C_II"),
                ],       
            ]
        ),
    )


