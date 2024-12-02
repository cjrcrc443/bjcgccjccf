import requests

from pyrogram import Client, filters

from AlinaXIQ import app


# API endpoint for Instagram video download
API_URL = "https://insta.savetube.me/downloadPostVideo"

# Regex pattern to match Instagram URLs
INSTAGRAM_URL_PATTERN = r"(https?://(?:www\.)?instagram\.com/(?:p|reel|tv)/[-a-zA-Z0-9@:%._\+~#=]{2,256})"

@app.on_message(filters.regex(INSTAGRAM_URL_PATTERN))
async def download_instagram_video(client, message):
    try:
        # Extract the Instagram URL
        instagram_url = message.text.strip()

        # Send the request to the API
        payload = {"url": instagram_url}
        headers = {"Content-Type": "application/json"}
        response = requests.post(API_URL, json=payload, headers=headers)

        # Check if the API response is successful
        if response.status_code != 200:
            await message.reply_text("❌ هەڵەیە لەگەڵ وێب سایتی داگرتن. تکایە دواتر هەوڵ بدە.")
            return

        # Parse the API response
        data = response.json()

        # Check if the required fields exist
        if "post_video_url" not in data:
            await message.reply_text("❌ نەتوانرا ڤیدیۆیەک بدۆزرێتەوە. تکایە لینکەکە دووبارە پشکنین بکە.")
            return

        # Extract the video URL and optional thumbnail
        video_url = data["post_video_url"]
        thumbnail_url = data.get("post_video_thumbnail")

        # Send a "downloading" message
        downloading_message = await message.reply_text("⬇ کەمێک چاوەڕێ بکە... ڤیدیۆیەک بەردەستکراوە.")

        # Send the video to the chat
        await client.send_video(
            chat_id=message.chat.id,
            video=video_url,
            caption="**✅ ڤیدیۆکە بە سەرکەوتوویی داگرترا. 📥\nلەلایەن: @HawalmusicBot**",
            thumb=thumbnail_url if thumbnail_url else None
        )

        # Delete the downloading message
        await downloading_message.delete()

    except requests.exceptions.RequestException as req_err:
        await message.reply_text(f"❌ هەڵەیە لەگەڵ وێب سایتی داگرتن.\n🔍 وردەکاری: {req_err}")
    except Exception as e:
        await message.reply_text(f"❌ هەڵەیەک ڕوویدا. 🔍 وردەکاری: {e}")
