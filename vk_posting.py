import vk_api


def post_to_vk(vk_token, album_id, group_id, message='', image_path=None,):
    vk_session = vk_api.VkApi(token=vk_token)
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk_session)
    if image_path:
        photo = upload.photo(  
            image_path,
            album_id=album_id,
            group_id=group_id
        )
        vk_photo_url = f"https://vk.com/photo{photo[0]['owner_id']}_{photo[0]['id']}"
        return vk.wall.post(
            owner_id=f'-{group_id}', 
            message=message, 
            attachments=f"photo{photo[0]['owner_id']}_{photo[0]['id']}"
        )
    return vk.wall.post(
        owner_id=f'-{group_id}', 
        message=message, 
    )
    