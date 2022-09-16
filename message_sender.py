import slack


def send_msg(msg):
    SLACK_TOKEN = 'xoxb-4093624051890-4087049777990-AoHHWi8oZgiU3e2l9J39fba9'

    client = slack.WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(channel='#크리스토퍼-공연-예매가-가능한지-알려줘요', text=msg)
