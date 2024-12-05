from pyrogram import filters

from AlinaXIQ import app
from strings.filters import command


@app.on_message(
    command(["بەستەر", "/link", "لینک", "لینك"]) & ~filters.bot & ~filters.private
)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("**سەرەتا بمکە ئەدمین**")
    await message.reply_text(
        f"**بە سەرکەوتوویی بەستەری گرووپ دروست کرا :**\n\n {invitelink}"
    )
