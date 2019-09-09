import vk_api
from requests.exceptions import ConnectionError
import os


def post_to_vk(vk_token, album_id, group_id, message='', image_path=None,):
    vk = vk_session.get_api()      
    attachments = get_attachments(vk_session, album_id, group_id, image_path)
    if not attachments:
        yield "Photo can't be uploaded to VK server"
    yield post_message_to_vk(vk, group_id, message, attachments)


def get_attachments(vk_session, album_id, group_id, image_path):
    if not image_path or not os.path.isfile(image_path):
        return
    try:
        upload = vk_api.VkUpload(vk_session)
        photo = upload.photo(  
            image_path,
            album_id=album_id,
            group_id=group_id
        )
        if not 'id' in photo[0]:
            return 
        return f"photo{photo[0]['owner_id']}_{photo[0]['id']}"
    except ConnectionError as error:
        return


def post_message_to_vk(vk_obj, group_id, message, attachments=None):
    try:
        vk_obj.wall.post(
            owner_id=f'-{group_id}', 
            message=message, 
            attachments=attachments,
        )
    except ConnectionError as error:
        return("Error occured, text can't be posted in VK due to "
            f"network connection errors: \n{error}")  

    