import requests 
from requests.exceptions import ConnectionError


def post_to_fb(token, group_id, message='', image_path=None ):
    image_obj = get_image_object(image_path)
    if not image_obj:
        yield "Photo can't be uploaded in FB" 
        try:
            response = post_only_text_to_fb(token, group_id, message)
            if not response.ok or 'id' not in response.json().keys():
                yield f"Error occured, post can't be published in FB:\n{response.json()}"
        except ConnectionError as error:
            yield f"Network error, post can't be published in FB: {error}"
    try:
        response = post_photo_and_text_to_fb(token, group_id, message, image_obj)
        if not response.ok or 'id' not in response.json().keys():
            yield f"Error occured, post can't be published in FB:\n{response.json()}"
    except ConnectionError as error:
        yield f"Network error, post can't be published in FB: {error}"
    

def get_image_object(image_path):
    try:
        image_object = open(image_path,'rb')
        return image_object
    except (OSError, IOError) as error:
        return   


def post_only_text_to_fb(token, group_id, message=''):
    url_text_template = 'https://graph.facebook.com/{page_id}/feed'
    response = requests.post(
        url_text_template.format(page_id = group_id),
        data = {
            'message': message,
            'access_token': token
        }  
    )
    return response


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