from AlinaXIQ import app

import os
import aiohttp
import tempfile
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Semaphore to limit the number of concurrent downloads
max_concurrent_downloads = 5
semaphore = asyncio.Semaphore(max_concurrent_downloads)

# Command to handle video downloading
@app.on_message(filters.command("download") & filters.private)
async def download_and_send_video(client, message):
    if len(message.command) < 2:
        await message.reply("Please provide a valid video link. Usage: `/download <video_url>`")
        return

    video_url = message.command[1]
    chat_id = message.chat.id

    # Send processing message
    downloading_message = await message.reply("Processing your request... Please wait.")

    # Download video within semaphore context
    async with semaphore:
        await download_video(video_url, chat_id, client, downloading_message)

# Function to download video and send it
async def download_video(video_url: str, chat_id: int, client, downloading_message):
    api_url = f'https://tele-social.vercel.app/down?url={video_url}'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                response.raise_for_status()
                content = await response.json()

        platform = content.get('platform', 'Unknown')
        video_link = content['data'].get('video')
        title = content['data'].get('title', f"{platform} Video")

        if not video_link or not video_link.startswith("http"):
            await client.send_message(chat_id, "Received an invalid video link.")
            return

        # Download the video
        async with aiohttp.ClientSession() as session:
            async with session.get(video_link) as response:
                response.raise_for_status()
                video_data = await response.read()

        # Save the video to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            temp_file.write(video_data)
            temp_file_path = temp_file.name

        # Send the video file to Telegram
        await client.send_video(chat_id, video=temp_file_path, caption=title)

        # Clean up the downloaded file
        os.remove(temp_file_path)

    except Exception as e:
        await client.send_message(chat_id, "Failed to download video. Please try again later.")
        print(f"Error: {e}")
    finally:
        # Delete the processing message
        await client.delete_messages(chat_id=chat_id, message_ids=[downloading_message.id])
