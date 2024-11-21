import re

import requests
from AlinaXIQ import app
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Mak

# Regex pattern to match Instagram URLs
instagram_url_pattern = r"(https?://(?:www\.)?instagram\.com/[-a-zA-Z0-9@:%._\+~#=]{2,256}/[-a-zA-Z0-9@:%._\+~#=]+)"


# To store sent video message URLs
sent_video_messages = {}


@app.on_message(filters.regex(instagram_url_pattern))
async def down(client, message):
    try:
        link = message.text
        json_data = {'url': link}
        response = requests.post('https://insta.savetube.me/downloadPostVideo', json=json_data).json()
        thu = response['post_video_thumbnail']
        video = response['post_video_url']

        # Sending the thumbnail with a button
        sent_message = await message.reply_photo(
            thu,
            reply_markup=Mak([[Btn("داگرتنی ڤیدیۆ", callback_data=f"vid:{message.message_id}")]])
        )
        sent_video_messages[sent_message.message_id] = video

    except Exception:
        await message.reply("**لینك هەڵەیە ئەزیزم**")


@app.on_callback_query(filters.regex(r"^vid:(\d+)$"))
async def all(client, callback_query):
    message_id = int(callback_query.data.split(":")[1])
    if message_id in sent_video_messages:
        video = sent_video_messages.pop(message_id)
        await callback_query.message.delete()
        caption = (
            "**✅ ꒐ بە سەرکەوتوویی داگرترا\n🎸 ꒐ @IQMCBOT**"
        )
        await app.send_video(callback_query.message.chat.id, video, caption=caption)
