# discord-telegram-bot
**Note:**
Automating user accounts is against the Discord ToS and puts your account at risk for deletion. This bot is a proof of concept and I do not recommend using it. Do so at your own risk.  

Simple Discord to Telegram one way forwarder, designed to work with user token for channels where bots are not permitted.

## Configuration
Set the fields accordingly in `keys.py`
- discord_channel: the discord id of the channel you want to forward.
- discord_token: discord user token.
- telegram_token: you can get this by speaking with @BotFather on telegram and creating a new bot.
- telegram_chatid: chatid of the telegram group you want to forward to.

## Installation
### Manually
Make sure [Python](https://www.python.org/downloads/) is installed on your system and open a terminal.
```
1. git clone https://github.com/dsymbol/discord-telegram-bot
2. pip install -r requirements.txt
3. python main.py
```
### Docker CLI
```
docker run -d -v `pwd`/keys.py:/app/keys.py dsymbol/discord-telegram-bot
```
