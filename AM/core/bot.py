import sys

from pyrogram import Client

import config

from ..logging import LOGGER



class AnonXBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting The Mission...")
        super().__init__(
            "SVDMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = get_me.first_name + " " + (get_me.last_name or "")

        try:
            await self.send_message(
                config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :**\n\n✨ 𝔻𝔸𝕋𝔸 : `{self.id}`\n❄ ᴘʀᴏꜰɪʟᴇ : {self.name}\n💫 UsᴇʀNᴀᴍE : @{self.username}"
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()

        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Please promote Bot as Admin in Logger Group"
            )
            sys.exit()
        LOGGER(__name__).info(f"SVDMusicBot Started as @{self.username}")
