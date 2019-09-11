import requests 
from requests.exceptions import ConnectionError
import os


class FBPostingError(Exception):
    pass


def post_to_fb(token, group_id, message, image_obj):
    try:
        response = post_photo_and_text_to_fb(token, group_id, message, image_obj)
    except ConnectionError as error:
        raise FBPostingError(f"Network error occured while posting in FB:\n{error}")
    if not response.ok or 'id' not in response.json().keys():
        raise FBPostingError(f"Error occured, post can't be published in FB:\n{response.json()}")
    

def post_photo_and_text_to_fb(token, group_id, message, image_obj):
    url_photo_template = 'https://graph.facebook.com/{page_id}/photos'
    response = requests.post(
        url_photo_template.format(page_id = group_id),
        files = {
            'files': image_obj
        },
        data = {
            'caption': message,
            'access_token': token
        }
    )
    return response