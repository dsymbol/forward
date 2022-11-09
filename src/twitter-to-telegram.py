"""
Name: twitter-to-telegram
Description: Stream tweets from any Twitter account to a Telegram Channel
"""

# ======================================================================================================================
# User Configuration: example values replace them with your own
# ======================================================================================================================

# Telegram BotFather created bot token
token = "1234567891:NrKveoWNZjDXR5lO9nUk_g8wmrNU3GsTmrS"
# Telegram channel id to src to easily obtained using https://t.me/chat_id_echo_bot
chat_id = -1001862553982
# Twitter v2 Bearer API Token https://developer.twitter.com/en
bearer_token = "AAAAAAAAAAAAAAAAAAAAALFSiwEAAAAA1habyTxWzpjmKDftpI87Trvh%2FPA09DtIJ0PIQ5K5sekAl7mBxgdUmf4alJaMYfqZqWdz3LdW8AQn5eV0"
# Twitter users to follow separated by commas
users = "LILUZIVERT,Cristiano"
# Only send tweets that have these words mentioned separated by commas, leave blank to src all tweets.
keywords = ""


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


DEPS = ["tweepy@git+https://github.com/tweepy/tweepy.git@b18c1a6239e81cb5744fa99d392ec539de787e5c",
        "python-telegram-bot==13.14"]

try:
    import tweepy
    from telegram import Bot, ParseMode
except (ModuleNotFoundError, ImportError):
    for dep in DEPS:
        install(dep)
    # Re-import after dependency installation
    import tweepy
    from telegram import Bot, ParseMode

# ----
# Code
# ----

import json


class DataStream(tweepy.StreamingClient):
    def on_data(self, raw_data):
        d = json.loads(raw_data)
        tweet_link = f"https://twitter.com/i/web/status/{d['data']['id']}"
        message = d['data']['text']
        author = [user['username'] for user in d['includes']['users']][0]
        prefix = f'Tweet \U0001F449 <a href="{tweet_link}">@{author}</a>'
        print(f"@{author}: {message}")
        message = f'{prefix}\n\n{message}'

        if keywords:
            if any(x in d['data']['text'] for x in keywords):
                tg.send_message(chat_id, message, parse_mode=ParseMode.HTML)
        else:
            tg.send_message(chat_id, message, parse_mode=ParseMode.HTML)


def delete_rules(_listener):
    _rules = _listener.get_rules()
    if _rules[0]:
        print("Deleting existing rules!")
        [listener.delete_rules(rule.id) for rule in _rules[0]]


def create_rules(_users):
    _users = ["from:" + user for user in _users]
    return tweepy.StreamRule(" OR ".join(_users))


if __name__ == "__main__":
    print(__doc__)
    chat_id = int(chat_id)
    users, keywords = users.split(","), keywords.split(",") if keywords else None
    tg = Bot(token=token)
    listener = DataStream(bearer_token, wait_on_rate_limit=True)
    delete_rules(listener)
    rules = create_rules(users)
    listener.add_rules(rules)
    print("Waiting for tweets...")
    listener.filter(expansions=['author_id'])
