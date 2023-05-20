from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" 𝒜𝒞𝒞𝐸𝒫𝒯 𝑀𝐸 𝐼𝒩 𝒴𝒪𝒰𝑅 𝐵𝒜𝒮𝐸 ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝓡𝓔𝓥𝓘𝓥𝓔-𝓗𝓔𝓛𝓟",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝒜𝒞𝒞𝐸𝒫𝒯 𝑀𝐸 𝐼𝒩 𝒴𝒪𝒰𝑅 𝐵𝒜𝒮𝐸",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝓡𝓔𝓥𝓘𝓥𝓔-𝓗𝓔𝓛𝓟", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❣ sᴜᴩᴩᴏʀᴛ ᴛʜᴇ ʙᴀꜱᴇ ❣", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🥀 🆆🅰🅽🆃🅴🅳 🥀", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ S͎E͎C͎R͎E͎T͎ ✨", 
                url="https://telegra.ph/file/712d384e549f37e74f4a8.mp4"
            )
        ],
     ]
    return buttons
