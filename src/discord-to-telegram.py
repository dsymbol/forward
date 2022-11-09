"""
Name: discord-to-telegram
Description: Forward messages from Discord channels to a Telegram channel,
designed to run as a user for channels where bots are not permitted.
"""

# ======================================================================================================================
# User Configuration: example values replace them with your own
# ======================================================================================================================

# Discord user token
discord_token = "gsHQ5wpRUHUiSScW1lq55iyr.H3XifBCbs8dmUxaYinen8rQcPyLDJgKoZK"
# Discord channel ids to src separated by commas
discord_channels = "123456789123456789,654321789123465889"
# Telegram BotFather created bot token
telegram_token = "1234567891:NrKSeoWNZjDXR5p99nUk_g8wmrNU3GsTmrS"
# Telegram channel id to src to, easily obtained using https://t.me/chat_id_echo_bot
telegram_chat_id = -1234567891234


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


DEPS = ["discord.py-self==1.9.2",
        "python-telegram-bot==13.14"]

try:
    import discord
    from telegram import Bot
except (ModuleNotFoundError, ImportError):
    for dep in DEPS:
        install(dep)
    # Re-import after dependency installation
    import discord
    from telegram import Bot

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
    print(__doc__)
    discord_channels = list(map(int, discord_channels.split(",")))
    telegram_chat_id = int(telegram_chat_id)
    print("Running, waiting for messages...")
    dc.run(discord_token)
