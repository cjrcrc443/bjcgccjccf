import re

import requests
from AlinaXIQ import app
import requests
from pyrogram import Client, filters

# Regex pattern to match Instagram URLs
instagram_url_pattern = r"(https?://(?:www\.)?instagram\.com/[-a-zA-Z0-9@:%._\+~#=]{2,256}/[-a-zA-Z0-9@:%._\+~#=]+)"

@app.on_message(filters.text & ~filters.private)
async def down(client, message):
    try:
        link = message.text
        json_data = {'url': link}
        response = requests.post('https://insta.savetube.me/downloadPostVideo', json=json_data).json()

        # Extract video and thumbnail
        thu = response['post_video_thumbnail']
        video = response['post_video_url']

        # Send thumbnail as a photo
        await message.reply_photo(thu, caption="*ڤیدیۆکە دابەزاندنی دەستپێدەکات...*\n\n⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - @MGIMT")

        # Send video directly
        caption = (
            "*بە سەرکەوتوویی داگرترا لەلایەن :\n"
            "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - @MGIMT\n\n"
            "@xv7amo - جۆینی ئەم کەناڵە شازە بکە♥️⚡️*"
        )
        await app.send_video(message.chat.id, video, caption=caption)

    except Exception as e:
        print(f"Error: {e}")
        await message.reply("**لینك هەڵەیە ئەزیزم**")
