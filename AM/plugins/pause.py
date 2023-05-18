from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from AM import app
from AM.core.call import Anon
from AM.utils.database import is_music_playing, music_off
from AM.utils.decorators import AdminRightsCheck
from AM.utils.inline.play import close_keyboard

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def iru_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Anon.Irru_Ley_Poduvom(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.first_name),
        reply_markup=close_keyboard
    )
