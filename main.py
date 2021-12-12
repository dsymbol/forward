from telegram import Bot
from keys import *  
import discord

dc = discord.Client()
tg = Bot(token=TELEGRAM_TOKEN)

@dc.event
async def on_message(message): 
    if message.channel.id in DISCORD_CHANNELS:
        if message.attachments:
            attachers = ""
            for attachment in message.attachments:
                attachers += f"{attachment} "
            print(f'{message.content} {attachers}')
            tg.sendMessage(TELEGRAM_CHAT_ID, f'{message.content} {attachers}')
        else:
            print(f"{message.content}")
            tg.sendMessage(TELEGRAM_CHAT_ID, message.content)

def main():
    print("Running, waiting for messages...")
    dc.run(DISCORD_TOKEN)

if __name__ == '__main__':
    main()
