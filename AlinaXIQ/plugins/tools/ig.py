import httpx
from bs4 import BeautifulSoup
import os
from pathlib import Path
from pyrogram import Client, filters
from AlinaXIQ import app

# Define headers to mimic the browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://saveig.app/en",
}

async def fetch_content(url):
    try:
        print(f"Fetching content from URL: {url}")
        async with httpx.AsyncClient(headers=HEADERS) as client:
            resp = await client.get(url)
            if resp.status_code == 200:
                return resp.text
            else:
                print(f"Failed to fetch content. Status code: {resp.status_code}")
                return None
    except Exception as e:
        print(f"Error fetching content: {e}")
        return None

async def extract_video_url(html_content):
    try:
        print("Extracting video URL from HTML content.")
        soup = BeautifulSoup(html_content, 'html.parser')
        video_tag = soup.find('meta', attrs={'property': 'og:video'})
        if video_tag and video_tag.get('content'):
            return video_tag['content']
        else:
            print("No video URL found in HTML content.")
            return None
    except Exception as e:
        print(f"Error extracting video URL: {e}")
        return None

async def download_video(url, destination_folder='/cache'):
    try:
        if not url:
            print("No URL provided to download.")
            return None

        print(f"Downloading video from URL: {url}")
        async with httpx.AsyncClient(headers=HEADERS) as client:
            resp = await client.get(url)
            if resp.status_code == 200:
                Path(destination_folder).mkdir(parents=True, exist_ok=True)
                filename = os.path.join(destination_folder, os.path.basename(url.split("?")[0]))
                with open(filename, 'wb') as file:
                    file.write(resp.content)
                print(f"Video saved to: {filename}")
                return filename
            else:
                print(f"Failed to download video. Status code: {resp.status_code}")
                return None
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

async def download_reel(instagram_url):
    try:
        print(f"Processing Instagram Reel URL: {instagram_url}")
        modified_url = instagram_url.replace("instagram.com", "ddinstagram.com")
        html_content = await fetch_content(modified_url)

        if html_content:
            video_url = await extract_video_url(html_content)
            if video_url:
                return await download_video(video_url)
            else:
                print("Failed to extract video URL.")
                return None
        else:
            print("Failed to fetch the page content.")
            return None
    except Exception as e:
        print(f"Error processing reel: {e}")
        return None

@app.on_message(filters.command("reel"))
async def reel_command_handler(client, message):
    if len(message.command) < 2:
        await message.reply("Please provide a Reel link. Usage: `/reel <link>`")
        return

    reel_link = message.command[1]
    if "instagram.com" not in reel_link:
        await message.reply("Invalid Instagram link. Please provide a valid Reel link.")
        return

    download_path = await download_reel(reel_link)

    if download_path and os.path.exists(download_path):
        try:
            await message.reply_video(
                video=open(download_path, 'rb'),
                caption="✅ Reel downloaded successfully!"
            )
            # Cleanup: Delete the video file after sending
            os.remove(download_path)
        except Exception as e:
            print(f"Error sending video: {e}")
            await message.reply("An error occurred while sending the video.")
    else:
        await message.reply("Sorry, I couldn't download the Reel. Please make sure the link is correct.")
