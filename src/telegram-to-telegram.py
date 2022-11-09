"""
Name: telegram-to-telegram
Description: Forward Telegram channel messages to others Telegram channels,
designed to run as a user for channels where bots are not permitted.
"""

# ======================================================================================================================
# User Configuration: example values replace them with your own
# ======================================================================================================================

# Both can be obtained here https://my.telegram.org
api_id = 12345
api_hash = "0123478789abcdef0123456789abcdef"
# Forwarding from and to channels separated by commas, leave either "" to get chat ids available on your account.
reading_channels = "1666884245"
writing_channels = "1726622217,1726622217"


# ======================================================================================================================
# Code: leave as is unless you know what you're doing
# ======================================================================================================================


def install(package):
    import subprocess
    import sys
    print(f"Installing {package} ...")
    command = [sys.executable, '-m', 'pip', 'install', package]
    p = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if p.returncode != 0:
        message = (
            f"Error running command!\n"
            f"Command: {p.args}\n"
            f"Error code: {p.returncode}\n"
            f"{p.stdout if len(p.stdout) > 0 else ''}\n"
            f"{p.stderr if len(p.stderr) > 0 else ''}"
        )
        raise RuntimeError(message)
    return p.returncode


DEPS = ["telethon@https://github.com/LonamiWebs/Telethon/archive/v1.24.zip",
        "cryptg~=0.3"]

try:
    from telethon import TelegramClient, events
    from telethon.tl.functions.messages import GetDialogsRequest
    from telethon.tl.types import InputPeerEmpty, MessageMediaUnsupported
except (ModuleNotFoundError, ImportError):
    for dep in DEPS:
        install(dep)
    # Re-import after dependency installation
    from telethon import TelegramClient, events
    from telethon.tl.functions.messages import GetDialogsRequest
    from telethon.tl.types import InputPeerEmpty, MessageMediaUnsupported

import os
import sys

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
