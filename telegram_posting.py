import telegram
from telegram.error import InvalidToken, TimedOut, NetworkError
from time import sleep


class TelegramPostingError(Exception):
    pass


def post_to_telegram(bot_token, chat_id, message, image_obj):
    try:
        bot = telegram.Bot(token=bot_token)
        response = post_text_to_telegram(bot, chat_id, message) 
        if not response.message_id:
            raise TelegramPostingError("Error occured while posting of text:\n"
                f"{response}")
        response = post_image_to_telegram(bot, chat_id, image_obj)
        if not response.message_id:
            raise TelegramPostingError("Error occured while posting of image:\n"
                f"{response}")        
    except InvalidToken as error:
        raise TelegramPostingError("Error occured while authentification "
            f"in Telegram: {error}") 
    except ConnectionError as error:
        raise TelegramPostingError("Network error while posting in Telegram:"
            f"\n{error}")


def post_text_to_telegram(bot, chat_id, message):
    try:
        return bot.send_message(chat_id=chat_id, text=message)
    except TimedOut as error:
        sleep(30)
        return bot.send_message(chat_id=chat_id, text=message)


def post_image_to_telegram(bot, chat_id, image_obj):
    try:
        return bot.send_photo(chat_id=chat_id, photo=image_obj)     
    except TimedOut as error:
        sleep(30)
        return bot.send_photo(chat_id=chat_id, photo=image_obj)


if __name__=='__main__':
    main()