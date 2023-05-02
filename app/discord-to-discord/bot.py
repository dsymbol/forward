import discord

from conf import *


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.channel.id in reading_channels:
            msg = message.content
            if message.attachments:
                for attachment in message.attachments:
                    msg += attachment + " "
            print(msg)
            for channel in writing_channels:
                channel = self.get_channel(channel)
                await channel.send(msg)


if __name__ == '__main__':
    reading_channels = list(map(int, reading_channels.split()))
    writing_channels = list(map(int, writing_channels.split()))
    client = MyClient()
    client.run(discord_token)
