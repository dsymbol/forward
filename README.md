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

```
git clone https://github.com/dsymbol/discord-telegram-bot
cd discord-telegram-bot
pip install -r requirements.txt
python main.py
```

### Docker CLI

```
git clone https://github.com/dsymbol/discord-telegram-bot
cd discord-telegram-bot
docker build -t discord-telegram-bot .
docker run -d -v `pwd`/keys.py:/app/keys.py discord-telegram-bot:latest
```

## Configuration

Edit `keys.py` accordingly:

| Variable                       | Description                                   |
| ------------------------------ | ----------------------------------------------|
| discord_channel                | id of discord channel you want to forward     |
| discord_token                  | discord user token                            |
| telegram_token                 | id of telegram chat you want to forward to    |
| telegram_chatid                | telegram bot token                            |
