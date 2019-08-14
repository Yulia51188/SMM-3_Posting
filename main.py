import os
from dotenv import load_dotenv
import vk_posting


def main():
    load_dotenv()
    vk_token = os.getenv("ACCESS_TOKEN")
    group_id = os.getenv("GROUP_ID")
    album_id = os.getenv("ALBUM_ID")
    print(album_id)
    print(vk_posting.post_to_vk(vk_token, album_id, group_id, 'rabbit.png', 'New message'))


if __name__=='__main__':
	main()