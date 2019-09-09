import requests 

def post_to_fb(token, group_id, message='', image_path=None ):
    # url_text_template = 'https://graph.facebook.com/{page_id}/feed'
    url_photo_template = 'https://graph.facebook.com/{page_id}/photos' 

    print(url_photo_template.format(page_id = fb_group_id))

    response = requests.post(
        url = url_photo_template.format(page_id = group_id),
        files = {
            'files': open(image_path,'rb')
        },
        data = {
            'caption': message,
            'access_token': token
        }
    )

    response.raise_for_status()
    print(response.json())


