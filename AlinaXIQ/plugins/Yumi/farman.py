from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AlinaXIQ import app
from strings.filters import command


@app.on_message(command(["ف1"]))
async def mmmezat(client, message):
    await message.reply_text(
        f"""**⧉ 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - فەرمانی بۆت🧑🏻‍💻🖤**\n••┉┉┉┉┉┉••🝢••┉┉┉┉┉┉••\n\n**بەخێربێی ئەزیزم {message.from_user.mention} بۆ بەشی داخستن و کردنەوەی فەرمان {MUSIC_BOT_NAME}**\n\n
** کردنەوەی + فەرمان 👾✅**

** ئایدی | وێنە **

** وەڵامدانەوە | ستیکەر **

      **زکر**

⩹⊶⊷⌯⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 •⧉⊶⊷⋗

** داخستنی + فەرمان 👾❎**

** ئایدی | وێنە **

** وەڵامدانەوە | ستیکەر **

      **زکر**

**نموونە : کردنەوەی ئایدی یان داخستنی ئایدی♥🧩**

**نموونە : کردنەوەی زکر یان داخستنی زکر♥🧩**

**@IQ7amo - 🖤👾باشترین بۆتی گۆرانی و پاراستن و وەڵامدانەوە**
**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 ", url=f"https://t.me/MGIMT"),
                ],
                [
                    InlineKeyboardButton("پڕۆگرامساز⚡", url=f"https://t.me/IQ7amo"),
                ],
            ]
        ),
    )
