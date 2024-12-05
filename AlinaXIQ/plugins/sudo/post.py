from pyrogram import filters

from AlinaXIQ import app
from config import OWNER_ID


@app.on_message(filters.command(["post"], prefixes=["/", "."]) & filters.user(OWNER_ID))
async def copy_messages(_, message):

    if message.reply_to_message:

        destination_group_id = -1001801583479

        await message.reply_to_message.copy(destination_group_id)
        await message.reply("𝗗𝗢𝗡𝗘✅")
