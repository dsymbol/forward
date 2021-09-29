# discord-telegram-bot
**Note:**
Automating user accounts is against the Discord ToS and puts your account at risk for deletion. This bot is a proof of concept and I do not recommend using it. Do so at your own risk.  

Simple Discord to Telegram one way forwarder, designed to work with user token for channels where bots are not permitted.
## Usage
Rename keys_example.py to keys.py and set the fields accordingly.
- discord_channel: the discord id of the channel you want to forward.
- discord_token: discord user token.
- telegram_token: You can get this by speaking with @BotFather on telegram and creating a new bot.
- telegram_chatid: chatid of the telegram group you want to forward to
## Installation
### Manually  
Clone the repo
```
git clone https://github.com/dsymbol/discord-telegram-bot
```
Install requirements
```
pip install -r requests.txt
```
Fill in your keys then run main.py
```
python main.py
```
### Docker CLI
```
docker run -d -v /localfolder/keys.py:/app/keys.py dsymbol/discord-telegram-bot
```
