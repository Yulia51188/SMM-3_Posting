import os
import vk_api


def main():
    vk_token = os.getenv("ACCESS_TOKEN")
    group_id = os.getenv("GROUP_ID")
    album_id = os.getenv("ALBUM_ID")

    vk_session = vk_api.VkApi(token=vk_token)
    vk = vk_session.get_api()
  
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo(  
        'rabbit_400x200.png',
        album_id=album_id,
        group_id=group_id
    )

    vk_photo_url = f"https://vk.com/photo{photo[0]['owner_id']}_{photo[0]['id']}"

    print(photo, '\nLink: ', vk_photo_url)
    print(vk.wall.post(
      owner_id=f'-{group_id}', 
      message='Hello world!', 
      attachments=f"photo{photo[0]['owner_id']}_{photo[0]['id']}")
    )


if __name__=='__main__':
    main()