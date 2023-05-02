import discord
from telegram import Bot

from conf import *

dc = discord.Client()
tg = Bot(token=telegram_token)


@dc.event
async def on_message(message):
    if message.channel.id in discord_channels:
        msg = message.content
        if message.attachments:
            for attachment in message.attachments:
                msg += attachment + " "
        print(msg)
        tg.send_message(telegram_chat_id, msg)


if __name__ == '__main__':
    discord_channels = list(map(int, discord_channels.split(",")))
    telegram_chat_id = int(telegram_chat_id)
    dc.run(discord_token)
