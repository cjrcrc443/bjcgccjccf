import requests
from AlinaXIQ import app
from pyrogram import filters

# Regex pattern to match Instagram URLs
instagram_url_pattern = r"(https?://(?:www\.)?instagram\.com/[-a-zA-Z0-9@:%._\+~#=]{2,256}/[-a-zA-Z0-9@:%._\+~#=]+)"


@app.on_message(filters.regex(instagram_url_pattern))
async def down(app, message):
    try:
        link = message.text
        json_data = {"url": link}
        response = requests.post(
            "https://insta.savetube.me/downloadPostVideo", json=json_data
        )

        # Check for response errors
        if response.status_code != 200:
            await message.reply("**هەڵەیە لەگەڵ وێبسایتی داگرتن. تکایە دواتر هەوڵ بدە.**")
            return

        data = response.json()

        # Ensure required keys exist
        if "post_video_thumbnail" not in data or "post_video_url" not in data:
            await message.reply("**نەتوانم ڤیدیۆ دابگرم. تکایە دڵنیابە لە ڕاستیەتی لینکەکە**")
            return

        thu = data["post_video_thumbnail"]
        video = data["post_video_url"]

        # Send thumbnail as a photo
        await message.reply_photo(
            thu,
            caption="**← کەمێک چاوەڕێ بکە .. ڤیدیۆ دادەبەزێت ...\n⧉• لەلایەن : @HawalmusicBot**",
        )

        # Send video directly
        caption = "**✅꒐ بە سەرکەوتوویی داگرترا\n🎸꒐ بۆتی @IQMCBOT**"
        await app.send_video(message.chat.id, video, caption=caption)

    except requests.exceptions.RequestException as req_err:
        print(f"Request Error: {req_err}")
        await message.reply("**هەڵەیە لەگەڵ وێب سایتی داگرتن. تکایە دواتر هەوڵ بدە.**")
    except KeyError as key_err:
        print(f"Key Error: {key_err}")
        await message.reply("**لینکەکە نادروستە یان پەیوەندی بە ڤیدیۆ نییە.**")
    except Exception as e:
        print(f"Error: {e}")
        await message.reply("**هەڵەیەک ڕوویدا. تکایە دواتر هەوڵ بدە.**")
