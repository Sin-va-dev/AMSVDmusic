import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Gettings Assistants Info...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("AbhiModszYT_Return")
                await self.one.join_chat("AM_YTSupport")
            except:
                pass
            assistants.append(1)
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            self.one.mention = get_me.mention
            assistantids.append(get_me.id)
            self.one.name = get_me.first_name + (get_me.last_name or "")

            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴏɴᴇ sᴛᴀʀᴛᴇᴅ :**\n\n✨ 𝔻𝔸𝕋𝔸 : `{self.one.id}`\n❄ ᴘʀᴏꜰɪʟᴇ : {self.one.name}\n💫 UsᴇʀNᴀᴍE : @{self.one.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Started as {self.one.name}"
            )
        if config.STRING2:
            await self.two.start()
            try:
                await self.one.join_chat("SVD_support_group")
                await self.one.join_chat("SVD_support_group")
            except:
                pass
            assistants.append(2)
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            self.two.mention = get_me.mention
            assistantids.append(get_me.id)
            self.two.name = get_me.first_name + (get_me.last_name or "")

            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴛᴡᴏ sᴛᴀʀᴛᴇᴅ :**\n\n✨ 𝔻𝔸𝕋𝔸 : `{self.two.id}`\n❄ ᴘʀᴏꜰɪʟᴇ : {self.two.name}\n💫 UsᴇʀNᴀᴍE : @{self.two.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Two Started as {self.two.name}"
            )
        if config.STRING3:
            await self.three.start()
            try:
                await self.one.join_chat("SVD_support_group")
                await self.one.join_chat("SVD_support_group")
            except:
                pass
            assistants.append(3)
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            self.three.mention = get_me.mention
            assistantids.append(get_me.id)
            self.three.name = get_me.first_name + (get_me.last_name or "")

            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴛʜʀᴇᴇ sᴛᴀʀᴛᴇᴅ :**\n\n✨ 𝔻𝔸𝕋𝔸  : `{self.three.id}`\n❄ ᴘʀᴏꜰɪʟᴇ : {self.three.name}\n💫 UsᴇʀNᴀᴍE : @{self.three.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Three Started as {self.three.name}"
            )
        if config.STRING4:
            await self.four.start()
            try:
                await self.one.join_chat("SVD_support_group")
                await self.one.join_chat("SVD_support_group")
            except:
                pass
            assistants.append(4)
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            self.four.mention = get_me.mention
            assistantids.append(get_me.id)
            self.four.name = get_me.first_name + (get_me.last_name or "")

            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ғᴏᴜʀ sᴛᴀʀᴛᴇᴅ :**\n\n✨ 𝔻𝔸𝕋𝔸  : `{self.four.id}`\n❄ ᴘʀᴏꜰɪʟᴇ : {self.four.name}\n💫 UsᴇʀNᴀᴍE : @{self.four.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Four Started as {self.four.name}"
            )
        if config.STRING5:
            await self.five.start()
            try:
                await self.one.join_chat("SVD_support_group")
                await self.one.join_chat("SVD_support_group")
            except:
                pass
            assistants.append(5)
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            self.five.mention = get_me.mention
            assistantids.append(get_me.id)
            self.five.name = get_me.first_name + (get_me.last_name or "")

            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ғɪᴠᴇ sᴛᴀʀᴛᴇᴅ :**\n\n✨  𝔻𝔸𝕋𝔸 : `{self.five.id}`\n❄ ᴘʀᴏꜰɪʟᴇ : {self.five.name}\n💫 UsᴇʀNᴀᴍE : @{self.five.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Five Started as {self.five.name}"
            )
