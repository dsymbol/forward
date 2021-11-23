from telegram import Bot
from keys import *  
import discord

dc = discord.Client()
tg = Bot(token=TELEGRAM_TOKEN)

@dc.event
async def on_message(message): 
    if message.channel.id in DISCORD_CHANNELS:
        print(f"[+] {message.content}")
        tg.sendMessage(TELEGRAM_CHAT_ID, message.content)

def main():
    print("[!] Bot running, waiting for messages...")
    dc.run(DISCORD_TOKEN)

if __name__ == '__main__':
    main()
