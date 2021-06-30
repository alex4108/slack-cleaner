import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv,find_dotenv
import time
import logging as log

load_dotenv(find_dotenv())
log.basicConfig(level=log.INFO)
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
channel_id = os.environ["SLACK_CHANNEL_ID"]

def clean(channel_id, cursor = None):
    try:
        if cursor == None:
            result = client.conversations_history(channel=channel_id, cursor=cursor)
        else:
            result = client.conversations_history(channel=channel_id)
        
        conversation_history = result["messages"]
        
        for msg in conversation_history:
            log.debug("Deleting: " + str(msg))
            if not do_delete(msg['ts']):
                time.sleep(5)
                if not do_delete(msg['ts']):
                    log.error("failed to delete: " + str(msg))

        if result.data['has_more']:
            clean(channel_id, result.data['response_metadata']['next_cursor'])

    except SlackApiError as e:
        log.error(str(e))
        log.error(f"Got an error retrieving conversations list: {e.response['error']}")

def do_delete(ts):
    try:
        response = client.chat_delete(
                channel=channel_id,
                ts=ts
        )
        return True
    except SlackApiError as e:
        return False

# This one just seeds a channel with messages, so you can test before releasing it :) 
def send_message():
    try:
        client.chat_postMessage(
                channel=channel_id,
                text="testing for spam"
        )
        return True
    except SlackApiError as e:
        return False


def spam_channel():
    spam_limit = 100
    i = 0
    log.info("Starting spam, going to send " + str(spam_limit) + " messages to channel.")
    while i < spam_limit:
        if not send_message():
            time.sleep(5)
            send_message()

        i = i + 1
    
    log.info("Spam complete")

def main():
    log.info(str(os.environ['SEND_SPAM']))
    if os.environ['SEND_SPAM'] == "1":
        spam_channel()

    log.info("Starting purge, this may take a while...")
    clean(channel_id)

if __name__ == "__main__":
    main()
    