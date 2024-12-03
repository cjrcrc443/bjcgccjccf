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
            video_url = video_tag['content']
            print(f"Video URL found: {video_url}")
            return video_url
        else:
            print("No 'og:video' meta tag found in HTML.")
            return None
    except Exception as e:
        print(f"Error in extract_video_url: {e}")
        return None

async def download_video(url, destination_folder='/cache'):
    try:
        if not url:
            print("No video URL provided.")
            return None

        print(f"Attempting to download video from: {url}")
        async with httpx.AsyncClient(headers=HEADERS) as client:
            resp = await client.get(url)
            if resp.status_code == 200:
                Path(destination_folder).mkdir(parents=True, exist_ok=True)
                filename = os.path.join(destination_folder, os.path.basename(url.split("?")[0]))
                with open(filename, 'wb') as file:
                    file.write(resp.content)
                print(f"Video saved at: {filename}")
                return filename
            else:
                print(f"Failed to download video. Status code: {resp.status_code}")
                return None
    except Exception as e:
        print(f"Error in download_video: {e}")
        return None


async def download_reel(instagram_url):
    try:
        print(f"Processing Instagram Reel URL: {instagram_url}")
        # Modify the URL
        modified_url = instagram_url.replace("instagram.com", "ddinstagram.com")
        print(f"Modified URL for scraping: {modified_url}")

        # Fetch the page content
        html_content = await fetch_content(modified_url)
        if not html_content:
            print("Failed to fetch HTML content.")
            return None

        # Extract the video URL
        video_url = await extract_video_url(html_content)
        if not video_url:
            print("No video URL could be extracted.")
            return None

        # Download the video
        download_path = await download_video(video_url)
        if not download_path:
            print("Video download failed.")
            return None

        print(f"Video successfully downloaded to: {download_path}")
        return download_path

    except Exception as e:
        print(f"Error in download_reel: {e}")
        return None

import re

INSTAGRAM_URL_REGEX = r"(https?://(?:www\.)?instagram\.com/.+)"

@app.on_message(filters.command("reel"))
async def reel_command_handler(client, message):
    if len(message.command) < 2:
        await message.reply("Please provide a Reel link. Usage: `/reel <link>`")
        return

    reel_link = message.command[1]
    if not re.match(INSTAGRAM_URL_REGEX, reel_link):
        await message.reply("Invalid Instagram link. Please provide a valid Reel link.")
        return

    download_path = await download_reel(reel_link)

    if download_path and os.path.exists(download_path):
        try:
            await message.reply_video(
                video=open(download_path, 'rb'),
                caption="✅ Reel downloaded successfully!"
            )
            os.remove(download_path)
        except Exception as e:
            print(f"Error sending video: {e}")
            await message.reply("An error occurred while sending the video.")
    else:
        await message.reply("Sorry, I couldn't download the Reel. Please make sure the link is correct.")
