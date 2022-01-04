
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 \n𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 \n𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 😎🤟 \n⭐𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 [亗『𝐊𝐀𝐓𝐈𝐋』亗 ](https://t.me/TERA_BAAP_KATIL)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰🥀𝐐𝐔𝐄𝐄𝐍💞❱", url="https://t.me/Harley_quinn65")
                  ],[
                    InlineKeyboardButton(
                        "❰𝗦𝘂𝗽𝗽𝗼𝗿𝘁🌎❱", url="https://t.me/heartbrokenperson1"
                    ),
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽🚩❱", url="https://t.me/FULL_MASTI_CLUBS"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❰🥀𝐊𝐢𝐍𝐆💞❱", url="https://t.me/TERA_BAAP_KATIL"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Esport") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**亗『𝐊𝐀𝐓𝐈𝐋』亗𝐌𝐮𝐬𝐢𝐜'𝐗 𝐎𝐧𝐥𝐢𝐧𝐞\n🌠꧁༺@TERA_BAAP_KATIL༻꧂ 🥀**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝘂𝗽𝗽𝗼𝗿𝘁❤️", url="https://t.me/heartbrokenperson1")
                ]
            ]
        )
   )
