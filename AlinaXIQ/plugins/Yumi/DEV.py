import os
from asyncio import gather

from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from AlinaXIQ import app
from config import USER_OWNER
from strings.filters import command


@app.on_message(command(["/source", "سۆرس"]))
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/b4ace5c5aec2901efed59.jpg",
        caption=f"""**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝙖𝙬𝙖𝙡 - 🧑🏻‍💻🖤 گەشەپێدەران](t.me/Haawall)**\n••┉┉┉┉┉••🝢••┉┉┉┉┉••\n**بەخێربێی ئەزیزم{message.from_user.mention} بۆ بەشی گەشەپێدەرانی بۆت🕷️•**\n**بۆ هەبوونی هەرکێشە و پرسیارێك پەیوەندی بە گەشەپێدەر بکە لەڕێگای دووگمەکانی خوارەوە♥•**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴱᴺᴺᴰﾂ🖇️🖤ᶜⁱᵗʸ", url=f"https://t.me/Hawaall"),
                ],
                [
                    InlineKeyboardButton(
                        "𐇮 ﮼ﺣ‌ّــەمــە 🇧🇷 𐇮", url=f"https://t.me/IQ7amo"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝙖𝙬𝙖𝙡", url=f"https://t.me/Haawall"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "『𓏺کەناڵی سەرەکی』", url=f"https://t.me/Haawall"
                    ),
                ],
            ]
        ),
    )


@app.on_message(
    filters.command(
        ["ڕێکخەری بۆت", "/bot", "بۆتی گۆرانی", "بۆت", "ڕێکخەر", "/maker"], ""
    )
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c8d0d49f5e13290314807.jpg",
        caption=f"""**● ڕێـكـخـەری بـۆتـی گـۆرانـی :\n⋆┄─┄─┄─┄─┄─┄─┄─┄⋆\n● بەخێربێی ئەزیزم {message.from_user.mention} 🕷️•\n● لە ڕێگای ئەم بۆتە دەتوانیت\n● بۆتی گۆرانی تایبەت بەخۆت دروستبکەیت\n● تایبەتمەندیەکانی بۆت\n● ڕێکڵام کردن، جۆینی ناچاری، گۆڕینی زانیاریەکانی بۆت\n● چالاککردن و ناچالاککردن\n● کۆنتڕۆڵکردنی ئەکاونتی یاریدەدەر**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "˹ᴍ ᴀ ᴋ ᴇ ꝛ ✗ ʜ ᴀ ᴡ ᴀ ʟ˼", url=f"https://t.me/creatmusicbot"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "ڕێـكـخـەری بـۆتـی گـۆرانـی", url=f"https://t.me/creatmusicbot"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "فێرکاری دروستکردن", url=f"https://t.me/ferkaredrsutkrdnebot/6"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝙖𝙬𝙖𝙡", url=f"https://t.me/Haawall"
                    ),
                ],
            ]
        ),
    )


@app.on_message(command(["@IQ7amo"]))
async def yas(client, message):

    usr = await client.get_chat("IQ7amo")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(
        photo,
        caption=f"**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙄𝙉𝘼 - سەرچاوەی زیرەك 🧑🏻‍💻](t.me/MGIMT)\nزانیاری گەشەپێدەری دووەمی بۆت\n↜︙𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙𝐈𝐃 ↬ :`{usr.id}`\n↜︙𝐁𝐈𝐎 ↬: {usr.bio}**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")],
            ]
        ),
    )


@app.on_message(command(["پڕۆگرامساز"]))
async def yas(client, message):
    usr = await client.get_chat("IQ7amo")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(
        photo,
        caption=f"**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 پڕۆگرامساز](t.me/MGIMT)\nزانیاری پڕۆگرامسازی سەرچاوە\n↜︙𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙𝐈𝐃 ↬ :`{usr.id}`\n↜︙𝐁𝐈𝐎 ↬: {usr.bio}**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")],
                [
                    InlineKeyboardButton(
                        "🝢 پەیوەندی کردن 🝢", url=f"https://t.me/{usr.username}"
                    ),
                ],
            ]
        ),
    )


@app.on_message(command(["سەرۆک", "@Hawaall", "گەشەپێدەر", "خاوەنی بۆت", "خاوەنی بوت"]))
async def yas(client, message):
    usr = await client.get_chat(USER_OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(
        photo,
        caption=f"**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝙖𝙬𝙖𝙡 - 🧑🏻‍💻🖤 خاوەنی بۆت](t.me/Haawall)\nزانیاری خاوەنی بۆت\n↜︙𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙𝐈𝐃 ↬ :`{usr.id}`\n↜︙𝐁𝐈𝐎 ↬: {usr.bio}**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")],
                [
                    InlineKeyboardButton(
                        "کەناڵی گەشەپێدەر", url=f"https://t.me/Haawall"
                    ),
                ],
            ]
        ),
    )


@app.on_message(command(["کەناڵ", "کەنال"]))
async def yas(client, message):
    usr = await client.get_chat(-1001665233883)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(
        photo,
        caption=f"**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝙖𝙬𝙖𝙡 - کەناڵی سەرچاوە 🧑🏻‍💻](t.me/Haawall)**\n**جۆینی کەناڵی بۆت بکە بۆ بینینی بابەتی جیاوازتر♥**\n\n** بەستەری کەناڵ :\nhttps://t.me/{usr.username}**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")],
            ]
        ),
    )


@app.on_message(command(["زیرەکی دەستکرد"]))
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7713aee1676f475d4ed21.jpg",
        caption=f"""**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝙖𝙬𝙖𝙡 - زیرەکی دەستکرد🧑🏻‍💻🖤](t.me/Haawall)**\n\n**بەخێربێی ئەزیزم {message.from_user.mention} بۆ بەشی زیرەکی دەستکرد تایبەت بە سەرچاوەی زیرەك**\n** بۆ بەکارهێنانی بنووسە : iq + پرسیارەکەت ♥⚡**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("﮼ᴱᴺᴺᴰﾂ🖇️🖤ᶜⁱᵗʸ", url=f"https://t.me/IQ7amo"),
                ],
                [
                    InlineKeyboardButton(
                        "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝘼𝙇𝙄𝙉𝘼", url=f"https://t.me/Haawall"
                    ),
                ],
            ]
        ),
    )


@app.on_message(command(["سەرۆکی گرووپ", "خاوەنی گرووپ", "owner"]) & filters.group)
async def gak_owne(client: Client, message: Message):
    if len(message.command) >= 2:
        return
    else:
        chat_id = message.chat.id

        async for member in client.get_chat_members(chat_id):
            if member.status == ChatMemberStatus.OWNER:
                id = member.user.id
                key = InlineKeyboardMarkup(
                    [[InlineKeyboardButton(member.user.first_name, user_id=id)]]
                )
                m = await client.get_chat(id)
                if m.photo:
                    photo = await app.download_media(m.photo.big_file_id)
                    return await message.reply_photo(
                        photo,
                        caption=f"**✧ ¦زانیاری خاوەن گرووپ \n\n ✧ ¦ ناو ← {m.first_name} \n ✧ ¦ یوزەر ← @{m.username} \n ✧ ¦ بایۆ ← {m.bio}**",
                        reply_markup=key,
                    )
                else:
                    return await message.reply("•" + member.user.mention)


@app.on_message(command(["گرووپ", "group"]) & filters.group)
async def ginnj(client: Client, message: Message):
    chat_idd = message.chat.id
    chat_name = message.chat.title
    chat_username = f"@{message.chat.username}"
    photo = await client.download_media(message.chat.photo.big_file_id)
    await message.reply_photo(
        photo=photo,
        caption=f"""**🦩 ¦ ꪀᥲ️ꪔᥱ » {chat_name}\n🐉 ¦ Ꭵժ ᘜᖇ᥆υρ »  -{chat_idd}\n🐊 ¦ ᥣᎥꪀk » {chat_username}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        chat_name, url=f"https://t.me/{message.chat.username}"
                    )
                ],
            ]
        ),
    )


@app.on_message(command(["گۆڕین", "گۆڕینی ستیکەر"]))
async def sticker_image(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("**ڕپلەی ستیکەر بکە**")
    if not reply.sticker:
        return await message.reply("**ڕپلەی ستیکەر بکە**")
    m = await message.reply("**کەمێك چاوەڕێبە . .**")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f), message.reply_document(f)])
    await m.delete()
    os.remove(f)


@app.on_message(command(["ناوم", "ناو"]) & filters.group)
async def vgdg(client: Client, message: Message):
    await message.reply_text(f"""•⎆┊** ناوت 🔥♥**»»  {message.from_user.mention()}""")
