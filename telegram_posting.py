import telegram

def post_to_vk(bot_token, chat_id, image_path=None, message=''):
	bot = telegram.Bot(token=bot_token)
	response_text = bot.send_message(chat_id=chat_id, text=message)
	yield response_text
    if image_path:
    	yield bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))

