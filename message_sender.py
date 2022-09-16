import slack

from dotenv import load_dotenv
import os

# load .env
load_dotenv()

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')


def send_msg(msg):
    client = slack.WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(channel='#크리스토퍼-공연-예매가-가능한지-알려줘요', text=msg)
