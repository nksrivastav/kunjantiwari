
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
ðð¡ð¢ð¬ ðð¬ ððð¯ðð§ðð ð¥ððð¥ðð ð«ðð¦ ðð®ð¬ð¢ð ð¶ ðð¨ð­ \nðð®ð§ ðð§ ðð«ð¢ð¯ðð­ð ð¥ ðð©ð¬ ð«ððð«ð¯ðð« ð \nðððð¥ â¤ï¸ ðð¢ð ð¡ ðð®ðð¥ð¢ð­ð² ðð®ð¬ð¢ð ð§ ðð§ ðð ðð¤ \nâ­ððð¯ðð¥ð¨ð©ðð ðð² [äºãðððððãäº ](https://t.me/TERA_BAAP_KATIL)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â°ð¥ððððððâ±", url="https://t.me/Harley_quinn65")
                  ],[
                    InlineKeyboardButton(
                        "â°ð¦ðð½ð½ð¼ð¿ððâ±", url="https://t.me/heartbrokenperson1"
                    ),
                    InlineKeyboardButton(
                        "â°ðð¿ð¼ðð½ð©â±", url="https://t.me/FULL_MASTI_CLUBS"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "â°ð¥ðð¢ðððâ±", url="https://t.me/TERA_BAAP_KATIL"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Esport") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**äºãðððððãäºðð®ð¬ð¢ð'ð ðð§ð¥ð¢ð§ð\nð ê§à¼º@TERA_BAAP_KATILà¼»ê§ ð¥**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¦ðð½ð½ð¼ð¿ðâ¤ï¸", url="https://t.me/heartbrokenperson1")
                ]
            ]
        )
   )
