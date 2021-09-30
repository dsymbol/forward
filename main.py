import discord
from telegram import Bot
from keys import *  

dc = discord.Client()
tg = Bot(token=telegram_token)
    
@dc.event
async def on_ready():
    print('Logged in as {0.user}'.format(dc))

@dc.event
async def on_message(message): 
    finalMessage = message.content
    if message.channel.id in discord_channel:
        print("Forwarding: " + finalMessage)
        tg.sendMessage(telegram_chatid, finalMessage)

dc.run(discord_token)
