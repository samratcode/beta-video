from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 
from helper.database import insert

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command("vcstart"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       insert(int(m.chat.id))
       await m.reply_text(f"**I am A BOT  Video Player And Group Management.\n\n**Type /vchelp To View Comands:-** __ \n1) Type /info To View Devs`",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Dev", url="https://t.me/Itz_Samrat")
                                    ]]
                            ))
   else:
      await m.reply_text(f"**Music Bot Online**")
                 reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Support", url="https://t.me/RukaSupport")
                                    ]]


@Client.on_message(filters.command("vcping"))
async def ping_pong(client, m: Message):
    start = time()
    m_reply = await m.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        " `PONG MF!!`\n"
        f" `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(filters.command("uptime"))
async def get_uptime(client, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        "bot Online:\n"
        f"• **uptime** `{uptime}`\n"
    )   
