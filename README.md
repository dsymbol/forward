# discord-telegram-bot
**Note:**
Automating user accounts is against the Discord ToS and puts your account at risk for deletion. This bot is a proof of concept and I do not recommend using it. Do so at your own risk.  

Simple Discord to Telegram one way forwarder, designed to work with user token for channels where bots are not permitted.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/) (If you intend on deploying the app as a Docker image)

## Install

There are two ways to begin using the bot, depending on your preference:

### Manual

```bash
git clone https://github.com/dsymbol/discord-telegram-bot
cd discord-telegram-bot
pip install -r requirements.txt
python main.py
```

### Docker CLI

```bash
git clone https://github.com/dsymbol/discord-telegram-bot
cd discord-telegram-bot
docker build -t discord-telegram-bot .
docker run -d -v `pwd`/keys.py:/app/keys.py discord-telegram-bot:latest
```

## Configuration

Before running the bot, you must first set it up so it can connect to the Discord and Telegram API. Create a keys.py file and fill in the following information:

- `DISCORD_TOKEN`: discord user token
- `DISCORD_CHANNELS`: channel ids to forward from
- `TELEGRAM_TOKEN`: telegram bot token
- `TELEGRAM_CHAT_ID`: telegram chat id to forward to