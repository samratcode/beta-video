from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("vchelp")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
Setting up
1) Add this Bot to your Group and Make it Admin 
2) Add @ThePyrogram to your Group 
Commands
=>> Vidio Playing 🎧
- /vplay : Reply to Video or File That You Want To stream In Vc.
- /end  : Stop the stream
- /search : To Get Link From Youtube
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Chat", url="https://t.me/RukaSupport"
                    )
                ]
            ]
        )
    )    
