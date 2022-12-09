import os
import sys

from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, MessageMediaUnsupported

client = TelegramClient('anon', api_id, api_hash)
client.start()


@client.on(events.NewMessage(chats=reading_channels))
async def message_handler(event):
    try:
        await event.client.get_entity(event.from_id)
    except:
        pass
    message = event.raw_text
    for i in writing_channels:
        print(f"Sending {message} to channel {i}")
        if event.media and not isinstance(event.media, MessageMediaUnsupported):
            print("Message has media")
            dl_media = await client.download_media(event.media)
            await client.send_file(i, dl_media, caption=message)
            os.remove(dl_media)
        else:
            await client.send_message(i, message)


async def get_chats():
    result = await client(GetDialogsRequest(offset_date=None,
                                            offset_id=0,
                                            offset_peer=InputPeerEmpty(),
                                            limit=20,
                                            hash=0))
    [print(f"{i.id} : {i.title}") for i in result.chats]
    [print(f"{i.id} : {i.first_name}") for i in result.users]


async def main():
    me = await client.get_me()
    print(f"Successfully logged in as {me.first_name}")
    if not reading_channels or not writing_channels:
        await get_chats()
        sys.exit("No reading or writing channel")
    print("Waiting for messages...")


if __name__ == "__main__":
    print(__doc__)
    api_id = int(api_id)
    reading_channels = list(map(int, reading_channels.split(",")))
    writing_channels = list(map(int, writing_channels.split(",")))
    try:
        with client:
            client.loop.run_until_complete(main())
            client.run_until_disconnected()
    except Exception as f:
        print(str(f))
