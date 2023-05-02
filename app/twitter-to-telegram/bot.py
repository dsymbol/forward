import json

import tweepy
from telegram import Bot, ParseMode

from conf import *

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
    chat_id = int(chat_id)
    users, keywords = users.split(","), keywords.split(",") if keywords else None
    tg = Bot(token=token)
    listener = DataStream(bearer_token, wait_on_rate_limit=True)
    delete_rules(listener)
    rules = create_rules(users)
    listener.add_rules(rules)
    print("Waiting for tweets...")
    listener.filter(expansions=['author_id'])
