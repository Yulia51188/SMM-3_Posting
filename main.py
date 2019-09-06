import os
from dotenv import load_dotenv
import vk_posting
import telegram_posting


def main():
    load_dotenv()
    vk_token = os.getenv("ACCESS_TOKEN")
    group_id = os.getenv("GROUP_ID")
    album_id = os.getenv("ALBUM_ID")
    vk_post_result = list(vk_posting.post_to_vk(
        vk_token, 
        album_id, 
        group_id, 
        'New message',
        'rabbit.png',
    ))
    if not any(vk_post_result):
        print('Text and image are posted in VK')
    else:
        for error_text in vk_post_result:
            if error_text: print(error_text)
    # bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    # chat_id = os.getenv("CHANNEL_ID")
    # telegram_post_result = list(telegram_posting.post_to_telegram(
    #     bot_token, 
    #     chat_id, 
    #     'New message',
    #     'rabbit.png'
    # ))
    # if not any(telegram_post_result):
    #     print('Text and image are posted in Telegram')
    # else:
    #     for error_text in telegram_post_result:
    #         if error_text: print(error_text)


if __name__=='__main__':
    main()