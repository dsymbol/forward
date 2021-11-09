import discord
from telegram import Bot
from keys import *  

dc = discord.Client()
tg = Bot(token=telegram_token)

@dc.event
async def on_message(message): 
    finalMessage = message.content
    if message.channel.id in discord_channel:
        print("[+] New message: " + finalMessage)
        tg.sendMessage(telegram_chatid, finalMessage)

def main():
    print("Bot running, waiting for messages...")
    dc.run(discord_token)

if __name__ == '__main__':
    main()
