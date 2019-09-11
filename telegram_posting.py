import telegram
from telegram.error import InvalidToken, TimedOut, NetworkError
import os
from dotenv import load_dotenv
from time import sleep


def post_to_telegram(bot_token, chat_id, message='', image_path=None):
    try:
        bot = telegram.Bot(token=bot_token)
    except InvalidToken as error:
        return(f"Error occured, message can't be posted in Telegram: {error}") 
    yield post_text_to_telegram(bot, chat_id, message) 
    yield post_image_to_telegram(bot, chat_id, image_path)


def post_text_to_telegram(bot, chat_id, message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
    except NetworkError as error:       
        return("Error occured, text can't be posted in Telegram due to " 
            f"network connection errors:\n{error}")  
    except TimedOut as error:
        sleep(30)
        bot.send_message(chat_id=chat_id, text=message)


def post_image_to_telegram(bot, chat_id, image_path):
    if not os.path.isfile(image_path):
        return("File doesn't exist")
    try:
        bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
    except NetworkError as error:
        return("Error occured, image can't be posted in Telegram due to " 
            f"network connection errors:\n{error}")  

    except TimedOut as error:
        sleep(30)
        bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))


def print_hello(message):
    print(f'Hello, {message}')


def main():
    load_dotenv()
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv("CHANNEL_ID")
    post_to_telegram(
        bot_token, 
        chat_id, 
        'Good morning'
        'rabbit.png' 
    )


if __name__=='__main__':
    main()