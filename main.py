from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    BotCommand,
    Message,
)
from os import environ, remove
from threading import Thread
from json import load
from re import search

# bot
with open("config.json", "r") as f:
    DATA: dict = load(f)


def getenv(var):
    return environ.get(var) or DATA.get(var, None)


bot_token = getenv("TOKEN")
api_hash = getenv("HASH")
api_id = getenv("ID")
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# start command
@app.on_message(filters.command(["start"]))
def send_start(
    client: Client,
    message: Message,
):
    app.send_message(
        message.chat.id,
        f"__👋 Hi **{message.from_user.mention}**, i am Link Bypasser Bot, just send me any supported links and i will you get you results.\nCheckout /help to Read More__"
                       
except UserNotParticipant:
        try:
            await cmd.reply_text(
                text="**Please Join My Updates Channel to use me!**\n\n"
                "Due to Overload, Only Channel Subscribers can use the Bot!",
                reply_markup=InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(
                            "🤖 Join Updates Channel",
                            url="t.me/bypassbot_update",
                        )
                    ],
                ]),
            )
            return 0
    )
    
# server loop
print("Bot Starting")
app.run()
